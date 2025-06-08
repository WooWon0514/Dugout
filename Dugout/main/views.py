from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from teams.models import Team, TeamStat  # 추가된 import

@login_required
def main_page(request):
    teams = Team.objects.all()

    # 승률 기준 정렬 (승 / (승+패+무)), 0으로 나누는 것 방지
    team_rankings = sorted(
        teams,
        key=lambda team: team.wins / (team.wins + team.losses + team.draws + 1e-5),
        reverse=True
    )

    # 상위 5개 팀 + 팀 스탯 정리
    team_data = []
    for team in team_rankings[:5]:
        try:
            stat = TeamStat.objects.get(team=team)
        except TeamStat.DoesNotExist:
            stat = None
        team_data.append({
            'name': team.name,
            'wins': team.wins,
            'losses': team.losses,
            'draws': team.draws,
            'games': team.wins + team.losses + team.draws,
            'win_rate': round(team.wins / (team.wins + team.losses + team.draws + 1e-5), 3),
            'batting_avg': getattr(stat, 'batting_avg', 'N/A'),
            'era': getattr(stat, 'era', 'N/A'),
        })

    return render(request, 'main/main.html', {'team_rankings': team_data})

@login_required
def player_ranking(request):
    return render(request, 'players/player_rankings.html')

@login_required
def team_info(request):
    return render(request, 'teams/team_list.html')
