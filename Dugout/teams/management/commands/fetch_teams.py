from django.core.management.base import BaseCommand
from teams.utils import fetch_and_save_teams

class Command(BaseCommand):
    help = 'STATIZ에서 팀 정보를 크롤링하여 저장합니다.'

    def handle(self, *args, **kwargs):
        fetch_and_save_teams()
        self.stdout.write(self.style.SUCCESS('팀 데이터 크롤링 완료 ✅'))