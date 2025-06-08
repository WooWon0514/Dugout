from django.core.management.base import BaseCommand
from players.models import Player
from players.utils import fetch_player_rankings

class Command(BaseCommand):
    help = "선수 인기순위 데이터를 크롤링하여 DB에 저장합니다."

    def handle(self, *args, **options):
        data = fetch_player_rankings()
        for item in data:
            player, _ = Player.objects.get_or_create(name=item["name"])
            player.views = item["views"]
            player.save()

        self.stdout.write(self.style.SUCCESS(f'{len(data)}명의 선수 데이터를 업데이트했습니다.'))
