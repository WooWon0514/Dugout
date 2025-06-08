소개
Dugout은 KBO 리그의 팀 및 선수 통계 데이터를 기반으로 다양한 정보를 제공하는 웹 서비스입니다.
- 인기순위
- 팀 순위
- 팀 상세 정보
- 선수 랭킹
등 다양한 통계를 제공하며,
로그인 기능 / 회원가입 기능 등을 지원합니다.

주요 기능
1. 로그인 / 회원가입 기능
- Django 기본 인증 지원
- Statiz API 토큰 발급 기능 구현

2. KBO 팀 정보
- 전체 팀 리스트
- 팀별 상세 페이지 (라인업, 승패, 득실점, WAA, WAR 등)
  
3. 선수 인기순위
- 선수 조회수 기반 인기 랭킹 표시

4. 구단별 선수 스탯
- 타자 / 투수 통합 랭킹 페이지 제공

Dugout/
├── Dugout/                # Django 프로젝트 설정
├── accounts/              # 사용자 인증 (로그인 / 회원가입)
├── players/               # 선수 데이터 관리
├── teams/                 # 팀 데이터 관리
├── templates/             # 템플릿 (HTML)
└── static/                 # 정적 파일 (CSS, JS 등)

## 구동 전 준비

1️. 프로젝트 클론 후 필수 패키지 설치 :

```bash
pip install -r requirements.txt

2. Statiz 데이터 수집 (터미널에서 명령어 실행) :
1) 전체 데이터 한 번에 등록하기
python manage.py import_all_data

2) 개별적으로 등록하기
# 선수 인기순위
python manage.py import_player_rankings

# 팀별 데이터
python manage.py import_lg_data
python manage.py import_doosan_data
python manage.py import_hanwha_data
python manage.py import_kia_data
python manage.py import_kiwoom_data
python manage.py import_kt_data
python manage.py import_lotte_data
python manage.py import_nc_data
python manage.py import_samsung_data
python manage.py import_ssg_data

3. 서버 실행
python manage.py runserver

메인 코드 설명

1. 로그인 기능
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import CustomAuthenticationForm, CustomUserCreationForm

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('/')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
- Django 기본 로그인 지원
- CustomAuthenticationForm 사용 → username + password 입력
- 회원가입 기능 지원
- 로그인 성공 시 메인 페이지 리다이렉트
  
2. 로그인 관련 URL 구성
# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'  

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
- /accounts/login/ → Django 기본 로그인
- /accounts/signup/ → 회원가입

3. 초기 데이터 준비 단계
아래 커맨드들을 반드시 실행하여 최초 데이터 수집을 진행하고,
이후 서버를 구동하면 정상적으로 팀/선수 데이터가 표시됩니다.
# 선수 인기순위 수집
python manage.py import_player_rankings

# 팀별 데이터 수집 (반드시 모든 팀 실행)
python manage.py import_lg_data
python manage.py import_doosan_data
python manage.py import_hanwha_data
python manage.py import_kia_data
python manage.py import_kiwoom_data
python manage.py import_kt_data
python manage.py import_lotte_data
python manage.py import_nc_data
python manage.py import_samsung_data
python manage.py import_ssg_data
  
4. 팀 데이터 수집 및 저장
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

import re
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

import requests

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
- Statiz 페이지에서 크롤링한 데이터를 DB에 저장
- update_or_create 사용으로 중복 없이 최신 데이터 유지

5. 선수 인기순위
# players/utils.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def fetch_player_rankings():
    options = Options()
    options.add_argument("--headless")  # 창 없이 실행
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://statiz.sporki.com/player/")
    time.sleep(3)  # 페이지 로딩 대기

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    rankings = []

    table = soup.find("table")  # 첫 번째 테이블 가져옴
    if not table:
        return rankings

    rows = table.find_all("tr")[1:]  # 첫 줄은 헤더니까 제외

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 3:
            rank = cols[0].text.strip()
            name = cols[1].text.strip()
            views = cols[2].text.strip().replace(",", "")
            rankings.append({
                "rank": int(rank),
                "name": name,
                "views": int(views)
            })

    return rankings

if __name__ == "__main__":
    players = fetch_player_rankings()
    for p in players:
        print(p)
        
- Selenium 사용해 Statiz 선수 인기순위 페이지 크롤링
- 조회수 기반 상위 20명 선수 표시 가능

6. 팀 상세 매치업 데이터 표시
# teams/models.py
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    wins = models.IntegerField()
    losses = models.IntegerField()
    draws = models.IntegerField()

    highlights = models.JSONField(default=dict)
    matchups = models.JSONField(default=dict)
    waa = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class TeamStat(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE)
    batting_avg = models.FloatField(null=True)
    homeruns = models.IntegerField(null=True)
    hits = models.IntegerField(null=True)
    stolen_bases = models.IntegerField(null=True)
    ops = models.FloatField(null=True)
    era = models.FloatField(null=True)
    whip = models.FloatField(null=True)
    strikeouts = models.IntegerField(null=True)

class VersusRecord(models.Model):
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='versus')
    opponent = models.CharField(max_length=50)
    wins = models.IntegerField()
    draws = models.IntegerField(default=0)
    losses = models.IntegerField()
    win_rate = models.FloatField()

class TeamWAR(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE)
    pitcher = models.FloatField()
    hitter = models.FloatField()
    bench = models.FloatField()
    defense = models.FloatField()
    
- 상대 팀별 승/무/패 데이터 → matchups JSON 저장
- 주요 스탯 → highlights JSON 저장
- WAR 관련 데이터 → waa JSON 저장

7. 템플릿 사용 예시
# teams/templates/teams/team_list.html
{% load humanize %}
{% load dict_filters %}
{% load math_filters %}

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>📊 팀 목록</title>
</head>
<body>
    <h2>📈 팀 리스트</h2>
    <table border="1">
        <thead>
            <tr>
                <th>팀</th>
                <th>승</th>
                <th>패</th>
                <th>무</th>
                <th>타율1위</th>
                <th>출루율1위</th>
                <th>장타율1위</th>
                <th>ERA1위</th>
            </tr>
        </thead>
        <tbody>
            {% for team in teams %}
            <tr>
                <td>{{ team.name }}</td>
                <td>{{ team.wins }}</td>
                <td>{{ team.losses }}</td>
                <td>{{ team.draws }}</td>
                <td>{{ team.highlights.타율1위 }}</td>
                <td>{{ team.highlights.출루율1위 }}</td>
                <td>{{ team.highlights.장타율1위 }}</td>
                <td>{{ team.highlights.ERA1위 }}</td>

            </tr>
            {% empty %}
            <tr><td colspan="8">데이터가 없습니다.</td></tr>
            {% endfor %}
        </tbody>
    </table>

    <h2>🏟️ 팀 정보</h2>
    <table border="1">
        <thead>
            <tr>
                <th>순위</th>
                <th>팀명</th>
                <th>경기수</th>
                <th>승</th>
                <th>무</th>
                <th>패</th>
                <th>승률</th>

            </tr>
        </thead>
        <tbody>
            {% for team in teams %}
            {% with total=team.wins|add:team.draws|add:team.losses %}
            <tr>
                <td>{{ forloop.counter }}</td>
                <td>{{ team.name }}</td>
                <td>{{ total|intcomma }}</td>
                <td>{{ team.wins }}</td>
                <td>{{ team.draws }}</td>
                <td>{{ team.losses }}</td>
                <td>
                    {% if total > 0 %}
                        {{ team.wins|div:total|floatformat:3 }}
                    {% else %}
                        0.000
                    {% endif %}
                </td>

            </tr>
            {% endwith %}
            {% empty %}
            <tr><td colspan="10">등록된 팀이 없습니다.</td></tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>

- 팀 주요 통계 및 성적을 테이블 형태로 표시
- highlights JSON을 활용하여 주간/시즌 MVP 표시 가능
