from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Import all player and team data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('▶ Importing team data...'))

        team_cmds = [
            'import_lg_data', 'import_doosan_data', 'import_hanwha_data',
            'import_kia_data', 'import_kiwoom_data', 'import_kt_data',
            'import_lotte_data', 'import_nc_data', 'import_samsung_data', 'import_ssg_data',
        ]

        for cmd in team_cmds:
            self.stdout.write(f'  - {cmd}')
            call_command(cmd)

        self.stdout.write(self.style.NOTICE('▶ Importing player rankings...'))
        call_command('import_player_rankings')

        self.stdout.write(self.style.SUCCESS('✅ 모든 선수 및 팀 데이터 import 완료!'))
