import pandas as pd
from .utils import recent_home_games, recent_away_games

def prepare_home_stats(rs, ts, n=5):    # prepares home team stats needed for shot model
    """ prepares home team stats needed for shot model """
    df = rs.get_results()
    home_features = df.loc[:, ["Div", "Date", "HomeTeam", "HST", "HSO", "HC", "AST", "ASO", "AC"]]

    # identify unique teams in the dataframe
    teams = home_features["HomeTeam"].unique()
    
    stats = list()
    for team_name in teams:
        filteredResults = recent_home_games(home_features, team_name, n)
        AvgHST = filteredResults.HST.mean()
        AvgHSO = filteredResults.HSO.mean()
        AvgHC = filteredResults.HC.mean()
        AvgAST = filteredResults.AST.mean()
        AvgASO = filteredResults.ASO.mean()
        AvgAC = filteredResults.AC.mean()

        stats.append({'HomeId': ts.get_team_id(team_name), 'HomeTeam': team_name, 'HAvgHST': AvgHST, 'HAvgHSO': AvgHSO, 'HAvgHC': AvgHC, 'HAvgAST': AvgAST, 'HAvgASO': AvgASO, 'HAvgAC': AvgAC})

    return pd.DataFrame(stats)

def prepare_away_stats(rs, ts, n=5):    # prepares away team stats needed for shot model
    """ prepares away team stats needed for shot model """
    
    df = rs.get_results()
    away_features = df.loc[:, ["Div", "Date", "AwayTeam", "HST", "HSO", "HC", "AST", "ASO", "AC"]]

    # identify unique teams in the dataframe
    teams = away_features["AwayTeam"].unique()

    stats = list()
    for team_name in teams:
        filteredResults = recent_away_games(away_features, team_name, n)
        AvgHST = filteredResults.HST.mean()
        AvgHSO = filteredResults.HSO.mean()
        AvgHC = filteredResults.HC.mean()
        AvgAST = filteredResults.AST.mean()
        AvgASO = filteredResults.ASO.mean()
        AvgAC = filteredResults.AC.mean()

        stats.append({'AwayId': ts.get_team_id(team_name), 'AwayTeam': team_name, 'AAvgHST': AvgHST, 'AAvgHSO': AvgHSO, 'AAvgHC': AvgHC, 'AAvgAST': AvgAST, 'AAvgASO': AvgASO, 'AAvgAC': AvgAC})

    return pd.DataFrame(stats)

def prepare_combined_stats(fs, rs, ts, n=5):    # prepares combined home and away team stats needed for shot model
    """ prepares combined home and away team stats needed for shot model based on a df of games"""

    home_stats = prepare_home_stats(rs, ts, n)
    away_stats = prepare_away_stats(rs, ts, n)

    fixtures = fs.get_fixtures()
    fixtures['HomeId'] = fixtures['home'].apply(ts.get_team_id)
    fixtures['AwayId'] = fixtures['away'].apply(ts.get_team_id)

    # merge home and away stats onto the list of games by Id
    fixtures_home_stats = fixtures.merge(home_stats, on = 'HomeId')
    fixtures_stats = fixtures_home_stats.merge(away_stats, on = 'AwayId')

    # calculate combined game stats
    fixtures_stats['HST'] = (fixtures_stats.HAvgHST + fixtures_stats.AAvgHST) / 2
    fixtures_stats['HSO'] = (fixtures_stats.HAvgHSO + fixtures_stats.AAvgHSO) / 2
    fixtures_stats['HC'] = (fixtures_stats.HAvgHC + fixtures_stats.AAvgHC) / 2
    fixtures_stats['AST'] = (fixtures_stats.AAvgAST + fixtures_stats.HAvgAST) / 2
    fixtures_stats['ASO'] = (fixtures_stats.AAvgASO + fixtures_stats.HAvgASO) / 2
    fixtures_stats['AC'] = (fixtures_stats.AAvgAC + fixtures_stats.HAvgAC) / 2

    # reduce to the required date items
    return fixtures_stats.loc[:, ['HomeId', 'HomeTeam', 'AwayId', 'AwayTeam', 'HST', 'HSO', 'HC', 'AST', 'ASO', 'AC']]
