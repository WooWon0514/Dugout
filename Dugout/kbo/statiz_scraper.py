import requests
from bs4 import BeautifulSoup

def fetch_top_players():
    url = "https://statiz.sporki.com/?opt=0&re=2"  # WAR TOP 10 페이지
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    players = []

    # WAR TOP 10 테이블 찾기
    war_table = soup.select_one("div:has(h5:contains('WAR TOP 10')) table")
    if war_table:
        rows = war_table.select("tbody tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) > 1:
                name = cols[1].text.strip()
                war = cols[2].text.strip()
                players.append((name, war))

    return players