def fixture_summary(fixture, ts, rs):
    home_team = ts.get_team(fixture['home'])
    away_team = ts.get_team(fixture['away'])
    summary = {}
    summary['fixture'] = fixture
    if not home_team is None:
        home_team_name = home_team['name']
        home_team_results = rs.get_team_results(home_team_name)
        home_team_btts = home_team_results['btts'][0:6].tolist()
        home_team_home_btts = home_team_results[home_team_results['HomeTeam'] == home_team_name]['btts'][0:6].tolist()
        summary['homeTeamBTTS'] = home_team_btts
        summary['homeTeamHomeBTTS'] = home_team_home_btts
    
    if not away_team is None:
        away_team_name = away_team['name']
        away_team_results = rs.get_team_results(away_team_name)
        away_team_btts = away_team_results['btts'][0:6].tolist()
        away_team_away_btts = away_team_results[away_team_results['AwayTeam'] == away_team_name]['btts'][0:6].tolist()
        summary['awayTeamBTTS'] = away_team_btts
        summary['awayTeamAwayBTTS'] = away_team_away_btts
    
    return summary

def fixture_summaries(fs, ts, rs):
    return list(map(lambda x: fixture_summary(x, ts, rs), fs.get_fixtures(format="list")))