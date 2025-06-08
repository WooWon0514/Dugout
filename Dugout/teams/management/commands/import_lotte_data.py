from django.core.management.base import BaseCommand
from teams.models import Team, TeamStat

class Command(BaseCommand):
    help = 'Import 롯데 자이언츠 team data'

    def handle(self, *args, **kwargs):
        # 기존 롯데 데이터 삭제
        Team.objects.filter(name="롯데 자이언츠").delete()

        matchups = {
            "KIA": {"승": 2, "무": 0, "패": 4, "승률": 0.333},
            "삼성": {"승": 5, "무": 0, "패": 3, "승률": 0.625},
            "두산": {"승": 2, "무": 0, "패": 3, "승률": 0.400},
            "SSG": {"승": 3, "무": 0, "패": 1, "승률": 0.750},
            "LG": {"승": 3, "무": 1, "패": 3, "승률": 0.500},
            "한화": {"승": 4, "무": 1, "패": 3, "승률": 0.571},
            "NC": {"승": 3, "무": 0, "패": 2, "승률": 0.600},
            "KT": {"승": 2, "무": 0, "패": 3, "승률": 0.400},
            "키움": {"승": 7, "무": 0, "패": 1, "승률": 0.875},
        }

        highlights = {
            "타율1위": "레이예스",
            "홈런1위": "레이예스",
            "타점1위": "레이예스",
            "출루율1위": "윤동희",
            "장타율1위": "레이예스",
            "OPS1위": "레이예스",
            "ERA1위": "박세웅",
            "WHIP1위": "박세웅",
            "세이브1위": "김용현",
            "홀드1위": "정해영"
        }

        waa = {
            "타자": 1.63,
            "투수": 0.64,
            "수비": 0.73,
            "선발": 1.55,
            "구원": 1.22,
        }

        lotte = Team.objects.create(
            name="롯데 자이언츠",
            wins=34,
            draws=2,
            losses=28,
            highlights=highlights,
            matchups=matchups,
            waa=waa
        )
        TeamStat.objects.create(
            team=lotte,
            batting_avg=0.268,
            era=4.10
        )

        self.stdout.write(self.style.SUCCESS("✅ 롯데 자이언츠 데이터 삽입 완료!"))