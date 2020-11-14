import numpy as np
import pandas as pd
from .utils import recent_home_games, recent_away_games 

def btts_home_form(rs, n=5):    # runs btts home form table for a country and season
    """ runs btts home form table for a country E or SC and season 20xxyy """

    # load the current seasons games
    all_games = rs.get_results()
    
    # reduce to only the columns needed for btts task
    home_features = all_games.loc[:,["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]]

    # add a column indicating btts occured in that game and split into a home and away table
    home_features["HBTTS"] = np.where((home_features["FTHG"] > 0) & (home_features["FTAG"] > 0),1,0)
    results = home_features[["Date", "HomeTeam", "HBTTS"]]
    
    # identify unique teams in the dataframe
    team_names = home_features["HomeTeam"].unique()
 
    team_hbtts = list()
    for team_name in team_names:
        filtered_results = recent_home_games(results, team_name, n)
        total_home_btts = filtered_results.HBTTS.sum()
        team_hbtts.append({'HomeTeam': team_name, 'HBTTS': total_home_btts})

    home_form_table = pd.DataFrame(team_hbtts)
    return home_form_table.sort_values(by="HBTTS", ascending=False)

def btts_away_form(rs, n=5):
    """ runs btts away form table for a country E or SC and season 20xxyy """

    # load the current seasons games
    all_games = rs.get_results()
    
    # reduce to only the columns needed for btts task
    away_features = all_games.loc[:,["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG"]]

    # add a column indicating btts occured in that game and split into a home and away table
    away_features["ABTTS"] = np.where((away_features["FTHG"] > 0) & (away_features["FTAG"] > 0),1,0)
    results = away_features[["Date", "AwayTeam", "ABTTS"]]
    
    # identify unique teams in the dataframe
    teams = away_features["AwayTeam"].unique()
 
    team_abtts = list()
    for team_name in teams:
        filteredResults = recent_away_games(results, team_name, n)
        total_away_btts = filteredResults.ABTTS.sum()
        team_abtts.append({'AwayTeam': team_name, 'ABTTS': total_away_btts})

    away_form_table = pd.DataFrame(team_abtts)
    return away_form_table.sort_values(by="ABTTS", ascending=False)