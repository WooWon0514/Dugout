from django.core.management.base import BaseCommand
from teams.models import Team

class Command(BaseCommand):
    help = 'Import SSG 랜더스 team data'

    def handle(self, *args, **kwargs):
        Team.objects.filter(name="SSG 랜더스").delete()

        matchups = {
            "KIA": {"승": 3, "무": 0, "패": 2, "승률": 0.600},
            "한화": {"승": 4, "무": 1, "패": 3, "승률": 0.571},
            "삼성": {"승": 4, "무": 0, "패": 1, "승률": 0.800},
            "두산": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "LG": {"승": 3, "무": 0, "패": 6, "승률": 0.333},
            "롯데": {"승": 5, "무": 0, "패": 0, "승률": 1.000},
            "NC": {"승": 2, "무": 0, "패": 4, "승률": 0.333},
            "KT": {"승": 4, "무": 0, "패": 1, "승률": 0.800},
            "키움": {"승": 2, "무": 0, "패": 4, "승률": 0.333}
        }

        highlights = {
            "타율1위": "최지훈",
            "홈런1위": "최정",
            "타점1위": "고명준",
            "출루율1위": "최정",
            "장타율1위": "최정",
            "OPS1위": "최정",
            "ERA1위": "조현영",
            "WHIP1위": "윤태현",
            "세이브1위": "조현영",
            "홀드1위": "노창운"
        }

        waa = {
            "타자": 0.77,
            "투수": 0.87,
            "수비": 0.43,
            "선발": 3.46,
            "구원": 1.63
        }

        Team.objects.create(
            name="SSG 랜더스",
            wins=38,
            draws=3,
            losses=28,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )

        self.stdout.write(self.style.SUCCESS("✅ SSG 랜더스 데이터 삽입 완료!"))