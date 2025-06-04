from django.core.management.base import BaseCommand
from teams.models import Team

class Command(BaseCommand):
    help = 'Import 키움 히어로즈 team data'

    def handle(self, *args, **kwargs):
        Team.objects.filter(name="키움 히어로즈").delete()

        matchups = {
            "KIA": {"승": 3, "무": 1, "패": 5, "승률": 0.375},
            "삼성": {"승": 0, "무": 0, "패": 5, "승률": 0.000},
            "두산": {"승": 3, "무": 0, "패": 5, "승률": 0.375},
            "SSG": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
            "LG": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
            "롯데": {"승": 1, "무": 0, "패": 7, "승률": 0.125},
            "한화": {"승": 3, "무": 0, "패": 5, "승률": 0.375},
            "NC": {"승": 2, "무": 0, "패": 4, "승률": 0.333},
            "KT": {"승": 2, "무": 0, "패": 7, "승률": 0.222}
        }

        highlights = {
            "타율1위": "류정현",
            "홈런1위": "송성윤",
            "타점1위": "송성윤",
            "출루율1위": "송성윤",
            "장타율1위": "송성윤",
            "OPS1위": "송성윤",
            "ERA1위": "콜펙더그",
            "WHIP1위": "콜펙더그",
            "세이브1위": "우상우",
            "홀드1위": "오세찬"
        }

        waa = {
            "타자": -5.31,
            "투수": -2.73,
            "수비": 2.37,
            "선발": -3.55,
            "구원": -0.65
        }

        Team.objects.create(
            name="키움 히어로즈",
            wins=17,
            draws=1,
            losses=45,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )

        self.stdout.write(self.style.SUCCESS("✅ 키움 히어로즈 데이터 삽입 완료!"))