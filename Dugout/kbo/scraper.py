# kbo/scraper.py

import requests
from bs4 import BeautifulSoup

def fetch_top10_players():
    url = "https://statiz.sporki.com/?opt=0&re=2"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    top10_table = soup.find("table", class_="table")
    rows = top10_table.find_all("tr")[1:11]  # 상위 10명만

    players = []

    for row in rows:
        cols = row.find_all("td")
        rank = cols[0].text.strip()
        name = cols[1].text.strip()
        war = cols[2].text.strip()
        team = cols[3].text.strip()

        players.append({
            "rank": rank,
            "name": name,
            "war": war,
            "team": team
        })

    return players

# kbo/scraper.py (위 내용 아래에 추가)

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dugout.settings")
django.setup()

from kbo.models import Player, Team

def save_top10_players():
    players = fetch_top10_players()
    for p in players:
        team_obj, _ = Team.objects.get_or_create(name=p["team"])
        Player.objects.create(
            name=p["name"],
            team=team_obj,
            position="IF",  # 기본값 설정 (필요시 수정)
            batting_average=0.0,
            games_played=0,
            home_runs=0,
            rbi=0
        )
    print("✅ 선수 10명 저장 완료")

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 스탯티즈 팀별 타율 페이지 (2024 시즌)
url = 'http://www.statiz.co.kr/stat.php?opt=0&sopt=1&re=0&ys=2024&ye=2024&se=0&te=0&tm=0&lg=1&po=0&ps=0&es=0&nm=1&cn=0&cv=0&ml=1&sn=30&vn=1'
headers = {'User-Agent': 'Mozilla/5.0'}

# 페이지 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 표 크롤링
table = soup.find('table', {'id': 'mytable'})
df = pd.read_html(str(table))[0]

# 불필요한 칼럼 정리 및 출력
df = df[df['팀명'] != '합계']  # '합계' 행 제거
df = df[['팀명', 'G', '타수', '안타', '타율', '홈런', '타점', 'OPS']]  # 주요 컬럼만
print(df)

# 원하면 CSV로 저장
df.to_csv('2024_team_batting.csv', index=False, encoding='utf-8-sig')