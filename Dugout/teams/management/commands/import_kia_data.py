from django.core.management.base import BaseCommand
from teams.models import Team, TeamStat

class Command(BaseCommand):
    help = 'Import KIA team data'

    def handle(self, *args, **kwargs):
        # 기존 KIA 팀 데이터 삭제
        Team.objects.filter(name="KIA 타이거즈").delete()

        matchups_data = {
            "삼성": {"승": 2, "무": 0, "패": 5, "승률": 0.286},
            "한화": {"승": 2, "무": 0, "패": 1, "승률": 0.667},
            "SSG": {"승": 2, "무": 0, "패": 3, "승률": 0.400},
            "LG": {"승": 2, "무": 0, "패": 3, "승률": 0.400},
            "롯데": {"승": 3, "무": 0, "패": 1, "승률": 0.750},
            "NC": {"승": 2, "무": 0, "패": 4, "승률": 0.333},
            "KT": {"승": 0, "무": 0, "패": 5, "승률": 0.000},
            "키움": {"승": 5, "무": 1, "패": 3, "승률": 0.625}
        }

        kia = Team.objects.create(
            name="KIA 타이거즈",
            wins=32,
            draws=11,
            losses=29,
            highlights={
                "타율1위": "최형우",
                "출루율1위": "최형우",
                "장타율1위": "최형우",
                "홈런1위": "최형우",
                "타점1위": "최형우",
                "도루1위": "박민호",
                "OPS1위": "최형우",
                "ERA1위": "최형우",
                "WHIP1위": "네일",
                "WAR1위": "최형우",
                "세이브1위": "조승우"
            },
            matchups=matchups_data,  # ✅ 여기가 핵심!
            waa={
                "투수": 0.76,
                "타자": 0.86,
                "벤치": 0.42,
                "수비": 2.10
            }
        )
        TeamStat.objects.create(
            team=kia,
            batting_avg=0.292,
            era=3.47
        )

        self.stdout.write(self.style.SUCCESS("✅ KIA 타이거즈 데이터 삽입 완료!"))