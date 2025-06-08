from django.core.management.base import BaseCommand
from teams.models import Team, TeamStat

class Command(BaseCommand):
    help = 'Import 삼성 라이온즈 team data'

    def handle(self, *args, **kwargs):
        Team.objects.filter(name="삼성 라이온즈").delete()

        matchups = {
            "KIA": {"승": 5, "무": 0, "패": 2, "승률": 0.714},
            "두산": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "SSG": {"승": 1, "무": 0, "패": 5, "승률": 0.167},
            "LG": {"승": 4, "무": 0, "패": 5, "승률": 0.444},
            "롯데": {"승": 3, "무": 0, "패": 4, "승률": 0.375},
            "한화": {"승": 2, "무": 0, "패": 4, "승률": 0.333},
            "NC": {"승": 2, "무": 0, "패": 2, "승률": 0.500},
            "KT": {"승": 2, "무": 0, "패": 2, "승률": 0.500},
            "키움": {"승": 5, "무": 0, "패": 0, "승률": 1.000}
        }

        highlights = {
            "타율1위": "김현준",
            "홈런1위": "다르엘",
            "타점1위": "다르엘",
            "출루율1위": "김현준",
            "장타율1위": "다르엘",
            "OPS1위": "다르엘",
            "ERA1위": "원태인",
            "WHIP1위": "원태인",
            "세이브1위": "문동주",
            "홀드1위": "김재윤"
        }

        waa = {
            "타자": 0.43,
            "투수": 0.63,
            "수비": 0.33,
            "선발": 3.52,
            "구원": 0.89
        }

        samsung = Team.objects.create(
            name="삼성 라이온즈",
            wins=31,
            draws=1,
            losses=28,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )
        TeamStat.objects.create(
            team=samsung,
            batting_avg=0.273,
            era=4.00
        )

        self.stdout.write(self.style.SUCCESS("✅ 삼성 라이온즈 데이터 삽입 완료!"))