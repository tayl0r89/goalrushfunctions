from .game_projections import game_projections
from .goal_rush_rating import goal_rush_ratings

def fixture_summary(fixture, ts, rs, projections, ratings):
    home_team = ts.get_team(fixture['home'])
    away_team = ts.get_team(fixture['away'])

    if home_team is None or away_team is None:
        return None

    summary = {}
    summary['fixture'] = fixture

    home_id = home_team['id']
    home_team_name = home_team['name']
    home_team_results = rs.get_team_results(home_team_name)
    home_team_btts = home_team_results['btts'][0:6].tolist()
    home_team_home_btts = home_team_results[home_team_results['HomeTeam'] == home_team_name]['btts'][0:6].tolist()
    summary['homeTeamBTTS'] = home_team_btts
    summary['homeTeamHomeBTTS'] = home_team_home_btts
    
    away_id = away_team['id']
    away_team_name = away_team['name']
    away_team_results = rs.get_team_results(away_team_name)
    away_team_btts = away_team_results['btts'][0:6].tolist()
    away_team_away_btts = away_team_results[away_team_results['AwayTeam'] == away_team_name]['btts'][0:6].tolist()
    summary['awayTeamBTTS'] = away_team_btts
    summary['awayTeamAwayBTTS'] = away_team_away_btts

    fixture_projections = projections[(projections['HomeId'] == home_id) & (projections['AwayId'] == away_id)]
    if fixture_projections.empty:
        return None
    
    game_stats = list()
    game_stats.append({'name': 'Home Win', 'value': fixture_projections['Home win'].iloc[0].item()})
    game_stats.append({'name': 'Draw', 'value': fixture_projections['Draw'].iloc[0].item()})
    game_stats.append({'name': 'Away Win','value': fixture_projections['Away win'].iloc[0].item()})

    btts_stats = list()
    btts_stats.append({'name': 'BTTTS', 'value': fixture_projections['BTTS'].iloc[0].item()})
    btts_stats.append({'name': 'Score Draw', 'value': fixture_projections['Score draw'].iloc[0].item()})
    btts_stats.append({'name': 'U2.5 Goals','value': fixture_projections['U2.5 goals'].iloc[0].item()})
    
    summary['gameStats'] = game_stats
    summary['bttsStats'] = btts_stats

    fixture_ratings = ratings[(ratings['HomeId'] == home_id) & (ratings['AwayId'] == away_id)]
    summary['rating'] = fixture_ratings['Rating'].iloc[0].item()

    return summary

def fixture_summaries(fs, ts, rs):
    projections = game_projections(fs, rs, ts)
    ratings = goal_rush_ratings(rs, fs, ts)
    summaries = list(map(lambda x: fixture_summary(x, ts, rs, projections, ratings), fs.get_fixtures(format="list")))
    return [summary for summary in summaries if not summary is None]
