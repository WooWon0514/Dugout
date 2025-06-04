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