import os
import sys

# 🟨 여기를 정확히 추가해! 'C:/Dugout'는 manage.py가 있는 폴더
sys.path.append("C:/Dugout")  # 또는 절대경로로 수정

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dugout.settings")

import django
django.setup()

from django.core.management.base import BaseCommand
from kbo.models import Player, Team
from kbo.statiz_scraper import fetch_top_players

class Command(BaseCommand):
    help = "Statiz에서 WAR TOP 10 선수 데이터를 불러옵니다"

    def handle(self, *args, **kwargs):
        players = fetch_top_players()
        for name, war in players:
            # 예시: "한화" 팀에 일단 모두 넣기
            team, _ = Team.objects.get_or_create(name="한화")
            Player.objects.update_or_create(
                name=name,
                team=team,
                defaults={
                    "position": "IF",  # 임시
                    "batting_average": 0,
                    "games_played": 0,
                    "home_runs": 0,
                    "rbi": 0,
                }
            )
        self.stdout.write(self.style.SUCCESS("선수 정보 업데이트 완료"))