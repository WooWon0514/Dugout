from django.core.management.base import BaseCommand
from teams.models import Team

class Command(BaseCommand):
    help = 'Import 한화 이글스 team data'

    def handle(self, *args, **kwargs):
        Team.objects.filter(name="한화 이글스").delete()

        matchups = {
            "KIA": {"승": 4, "무": 0, "패": 1, "승률": 0.800},
            "한화": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
            "삼성": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
            "SSG": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
            "LG": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "롯데": {"승": 3, "무": 0, "패": 4, "승률": 0.429},
            "NC": {"승": 6, "무": 0, "패": 3, "승률": 0.667},
            "KT": {"승": 2, "무": 0, "패": 3, "승률": 0.375},
            "키움": {"승": 5, "무": 0, "패": 1, "승률": 0.833}
        }

        highlights = {
            "타율1위": "문현빈",
            "홈런1위": "노시환",
            "타점1위": "노시환",
            "출루율1위": "문현빈",
            "장타율1위": "노시환",
            "OPS1위": "문현빈",
            "ERA1위": "문동주",
            "WHIP1위": "문동주",
            "세이브1위": "김서현",
            "홀드1위": "정해원"
        }

        waa = {
            "타자": 2.13,
            "투수": -0.13,
            "수비": 0.36,
            "선발": 5.06,
            "구원": 1.85
        }

        Team.objects.create(
            name="한화 이글스",
            wins=36,
            draws=0,
            losses=26,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )

        self.stdout.write(self.style.SUCCESS("✅ 한화 이글스 데이터 삽입 완료!"))