# teams/utils.py
import requests
from bs4 import BeautifulSoup
from .models import Team

def fetch_and_save_teams():
    url = "https://statiz.sporki.com/team/"
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    # 팀 div들 (색깔 박스들)
    team_boxes = soup.select('div[data-v-0f6c35f6] > div.flex-auto')  # 정확한 구조에 따라 유동적일 수 있음

    for box in team_boxes:
        name_tag = box.select_one('div span')
        record_tag = box.select_one('div span + span')

        if not name_tag or not record_tag:
            continue

        name = name_tag.text.strip()
        record = record_tag.text.strip()

        # 기록 예: "82승 12무 91패"
        wins, draws, losses = 0, 0, 0
        try:
            wins = int(record.split("승")[0])
            draws = int(record.split("승")[1].split("무")[0].strip())
            losses = int(record.split("무")[1].split("패")[0].strip())
        except Exception as e:
            print(f"⚠️ 파싱 에러: {record}, error: {e}")
            continue

        total_games = wins + draws + losses
        win_rate = round(wins / total_games, 3) if total_games > 0 else 0.0

        Team.objects.update_or_create(
            name=name,
            defaults={
                'wins': wins,
                'draws': draws,
                'losses': losses,
                'win_rate': win_rate
            }
        )

import requests
from bs4 import BeautifulSoup

def get_team_codes():
    url = "https://statiz.sporki.com/team/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    teams = []
    for div in soup.select('div.accordion-item'):
        link_tag = div.find('a', href=True)
        name = div.select_one('strong').text.strip() if div.select_one('strong') else "UNKNOWN"
        if link_tag and 't_code=' in link_tag['href']:
            t_code = link_tag['href'].split('t_code=')[1].split('&')[0]
            teams.append({
                'name': name,
                't_code': t_code
            })

    return teams

# teams/utils.py (계속)

import re

def fetch_team_details(t_code):
    url = f"https://statiz.sporki.com/team/?m=team&t_code={t_code}&year=2025"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    # ✅ 팀명 + 승/패/무
    header = soup.select_one('div.team_header strong')
    title = header.text.strip() if header else ''
    team_name_match = re.match(r'\d+\s+(.*)', title)
    team_name = team_name_match.group(1) if team_name_match else title

    record_text = header.find_next('div').text if header else ''
    record_match = re.search(r'(\d+)승\s+(\d+)패\s+(\d+)무', record_text)
    win, loss, draw = map(int, record_match.groups()) if record_match else (0, 0, 0)

    # ✅ 주요 타이틀
    highlights = {}
    for tr in soup.select('.record_right table')[0].select('tr'):
        td = tr.select('td')
        if len(td) == 3:
            key = td[0].text.strip()
            player = td[1].text.strip()
            value = td[2].text.strip()
            highlights[key] = (player, value)

    # ✅ 상대전적
    matchup_stats = {}
    for row in soup.select('.record_right table')[1].select('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) >= 5:
            opponent = cols[0].text.strip()
            win = int(cols[1].text.strip())
            draw = int(cols[2].text.strip())
            lose = int(cols[3].text.strip())
            ratio = cols[4].text.strip()
            matchup_stats[opponent] = {'win': win, 'draw': draw, 'lose': lose, 'rate': ratio}

    return {
        'name': team_name,
        'record': {'win': win, 'loss': loss, 'draw': draw},
        'highlights': highlights,
        'matchups': matchup_stats,
    }

# utils.py 내부에 추가

def fetch_and_save_all_team_data():
    from .models import Team  # 필요한 경우만 import
    teams = get_team_codes()

    for team in teams:
        t_code = team['t_code']
        name = team['name']
        print(f"📥 Fetching {name}...")

        try:
            details = fetch_team_details(t_code)

            # 모델에 저장 (있으면 update, 없으면 create)
            Team.objects.update_or_create(
                name=details['name'],
                defaults={
                    'wins': details['record']['win'],
                    'losses': details['record']['loss'],
                    'draws': details['record']['draw'],
                    'highlights': details['highlights'],  # JSONField
                    'matchups': details['matchups'],      # JSONField
                    'waa': details['waa'],                # JSONField
                }
            )
            print(f"✅ Saved: {details['name']}")

        except Exception as e:
            print(f"❌ Failed {name}: {e}")


# teams/utils.py
import requests
from bs4 import BeautifulSoup


def fetch_team_data(team_code: str = '2002', year: int = 2025):
    """
    statiz.sporki.com 사이트에서 팀 정보를 크롤링해 dict로 반환한다.
    기본값은 KIA 타이거즈 (해태 포함).
    """
    url = f'https://statiz.sporki.com/team/?m=team&t_code={team_code}&year={year}'
    response = requests.get(url)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'html.parser')

    # 테이블에서 데이터 추출 (기본적인 예시)
    data_table = soup.find('table', class_='team-data')  # class 이름은 실제 HTML 구조에 맞게 수정
    rows = data_table.find_all('tr')

    team_info = {}

    for row in rows:
        cells = row.find_all(['th', 'td'])
        if len(cells) != 2:
            continue
        label = cells[0].text.strip()
        value = cells[1].text.strip().replace(',', '')
        team_info[label] = value

    return team_info

# teams/utils.py

from .constants import TEAM_CODES

def fetch_all_teams_data(year: int = 2025):
    all_team_data = []

    for team_name, team_code in TEAM_CODES.items():
        print(f'🔄 Fetching {team_name}...')
        try:
            data = fetch_team_data(team_code=team_code, year=year)
            data['name'] = team_name
            all_team_data.append(data)
        except Exception as e:
            print(f'❌ {team_name} 실패: {e}')

    return all_team_data

# teams/utils.py

from .models import Team

def save_team_data(team_data_list):
    for data in team_data_list:
        team, _ = Team.objects.update_or_create(
            name=data.get('name'),
            defaults={
                'wins': int(data.get('승', 0)),
                'losses': int(data.get('패', 0)),
                'draws': int(data.get('무', 0)),
                'win_rate': float(data.get('승률', 0)),
                'games_behind': data.get('게임차', ''),
                'runs_scored': int(data.get('득점', 0)),
                'runs_allowed': int(data.get('실점', 0)),
                'team_batting_avg': float(data.get('팀타율', 0)),
                'team_era': float(data.get('팀ERA', 0)),
            }
        )
