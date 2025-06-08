from django.core.management.base import BaseCommand
from teams.models import Team, TeamStat

class Command(BaseCommand):
    help = 'Import 두산 베어스 team data'

    def handle(self, *args, **kwargs):
        Team.objects.filter(name="두산 베어스").delete()

        matchups = {
            "KIA": {"승": 1, "무": 0, "패": 7, "승률": 0.125},
            "삼성": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "SSG": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "LG": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "롯데": {"승": 2, "무": 0, "패": 3, "승률": 0.400},
            "한화": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
            "NC": {"승": 1, "무": 2, "패": 3, "승률": 0.250},
            "KT": {"승": 2, "무": 0, "패": 3, "승률": 0.400},
            "키움": {"승": 5, "무": 0, "패": 3, "승률": 0.625},
        }

        highlights = {
            "타율1위": "정현석",
            "홈런1위": "양석환",
            "타점1위": "양석환",
            "출루율1위": "정현석",
            "장타율1위": "양석환",
            "OPS1위": "정현석",
            "ERA1위": "장원준",
            "WHIP1위": "장원준",
            "세이브1위": "김광현",
            "홀드1위": "박치국"
        }

        waa = {
            "타자": 0.07,
            "투수": 0.87,
            "수비": 0.33,
            "선발": 3.45,
            "구원": 1.32
        }

        doosan = Team.objects.create(
            name="두산 베어스",
            wins=29,
            draws=1,
            losses=34,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )
        TeamStat.objects.create(
            team=doosan,
            batting_avg=0.271,
            era=3.98
        )

        self.stdout.write(self.style.SUCCESS("✅ 두산 베어스 데이터 삽입 완료!"))