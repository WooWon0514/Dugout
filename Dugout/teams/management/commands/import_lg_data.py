from django.core.management.base import BaseCommand
from teams.models import Team, TeamStat

class Command(BaseCommand):
    help = 'Import LG 트윈스 team data'

    def handle(self, *args, **kwargs):
        # 기존 데이터 삭제
        Team.objects.filter(name="LG 트윈스").delete()

        matchups = {
            "KIA": {"승": 3, "무": 0, "패": 2, "승률": 0.600},
            "삼성": {"승": 1, "무": 0, "패": 4, "승률": 0.200},
            "두산": {"승": 3, "무": 0, "패": 0, "승률": 1.000},
            "SSG": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
            "롯데": {"승": 3, "무": 1, "패": 1, "승률": 0.750},
            "한화": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "NC": {"승": 4, "무": 0, "패": 3, "승률": 0.571},
            "KT": {"승": 0, "무": 0, "패": 3, "승률": 0.000},
            "키움": {"승": 5, "무": 0, "패": 1, "승률": 0.833},
        }

        highlights = {
            "타율1위": "문보경",
            "홈런1위": "오스틴",
            "타점1위": "오스틴",
            "출루율1위": "문보경",
            "장타율1위": "오스틴",
            "OPS1위": "오스틴",
            "ERA1위": "송승기",
            "WHIP1위": "임찬규",
            "세이브1위": "지하스",
            "홀드1위": "김정현",
        }

        waa = {
            "타자": 4.58,
            "투수": 5.04,
            "수비": 1.34,
            "선발": 4.30,
            "구원": 1.58,
        }

        lg = Team.objects.create(
            name="LG 트윈스",
            wins=36,
            draws=1,
            losses=23,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )
        TeamStat.objects.create(
            team=lg,
            batting_avg=0.285,
            era=3.21
        )

        self.stdout.write(self.style.SUCCESS("✅ LG 트윈스 데이터 삽입 완료!"))