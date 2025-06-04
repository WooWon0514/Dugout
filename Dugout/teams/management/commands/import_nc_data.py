from django.core.management.base import BaseCommand
from teams.models import Team

class Command(BaseCommand):
    help = 'Import NC 다이노스 team data'

    def handle(self, *args, **kwargs):
        Team.objects.filter(name="NC 다이노스").delete()

        matchups = {
            "KIA": {"승": 2, "무": 0, "패": 2, "승률": 0.500},
            "삼성": {"승": 2, "무": 0, "패": 4, "승률": 0.333},
            "두산": {"승": 3, "무": 0, "패": 1, "승률": 0.750},
            "SSG": {"승": 1, "무": 0, "패": 4, "승률": 0.200},
            "LG": {"승": 3, "무": 0, "패": 2, "승률": 0.600},
            "롯데": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "한화": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
            "KT": {"승": 3, "무": 0, "패": 3, "승률": 0.500},
            "키움": {"승": 4, "무": 0, "패": 2, "승률": 0.667},
        }

        highlights = {
            "타율1위": "박민우",
            "홈런1위": "김주원",
            "타점1위": "김주원",
            "출루율1위": "김성욱",
            "장타율1위": "김주원",
            "OPS1위": "김주원",
            "ERA1위": "리앤드리",
            "WHIP1위": "리앤드리",
            "세이브1위": "류진욱",
            "홀드1위": "백재현",
        }

        waa = {
            "타자": 0.73,
            "투수": -0.33,
            "수비": -0.37,
            "선발": -0.37,
            "구원": 0.33
        }

        Team.objects.create(
            name="NC 다이노스",
            wins=29,
            draws=0,
            losses=32,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )

        self.stdout.write(self.style.SUCCESS("✅ NC 다이노스 데이터 삽입 완료!"))