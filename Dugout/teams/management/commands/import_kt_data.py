from django.core.management.base import BaseCommand
from teams.models import Team, TeamStat

class Command(BaseCommand):
    help = 'Import KT 위즈 team data'

    def handle(self, *args, **kwargs):
        # 기존 KT 데이터 제거
        Team.objects.filter(name="KT 위즈").delete()

        matchups = {
            "KIA": {"승": 5, "무": 0, "패": 4, "승률": 0.556},
            "삼성": {"승": 6, "무": 0, "패": 2, "승률": 0.750},
            "두산": {"승": 6, "무": 1, "패": 2, "승률": 0.750},
            "SSG": {"승": 1, "무": 0, "패": 4, "승률": 0.200},
            "LG": {"승": 3, "무": 0, "패": 2, "승률": 0.600},
            "롯데": {"승": 1, "무": 2, "패": 3, "승률": 0.333},
            "한화": {"승": 2, "무": 0, "패": 3, "승률": 0.400},
            "NC": {"승": 2, "무": 0, "패": 4, "승률": 0.333},
            "키움": {"승": 7, "무": 0, "패": 2, "승률": 0.778},
        }

        highlights = {
            "타율1위": "황재균",
            "홈런1위": "안현민",
            "타점1위": "안현민",
            "출루율1위": "황재균",
            "장타율1위": "로하스",
            "OPS1위": "로하스",
            "ERA1위": "소형준",
            "WHIP1위": "오원석",
            "세이브1위": "고영표",
            "홀드1위": "박영현",
        }

        waa = {
            "타자": 1.34,
            "투수": 0.53,
            "수비": 0.29,
            "선발": 3.47,
            "구원": 2.05,
        }

        kt = Team.objects.create(
            name="KT 위즈",
            wins=30,
            draws=3,
            losses=31,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )
        TeamStat.objects.create(
            team=kt,
            batting_avg=0.275,
            era=3.85
        )

        self.stdout.write(self.style.SUCCESS("✅ KT 위즈 데이터 삽입 완료!"))