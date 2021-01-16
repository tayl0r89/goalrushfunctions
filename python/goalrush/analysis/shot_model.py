import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from .team_stats import prepare_combined_stats

def train_fthg_model(rs):
    """ calculates the parameters for the model based on historic data"""
    # load dataframe of past data for the predictive model
    df = rs.get_results(current_season_only=False)
    # set up the model
    modelFTHG = smf.ols(formula='FTHG ~ HST + HSO + HC', data=df)
    return modelFTHG.fit()

def train_ftag_model(rs):    # calculates the parameters for the model based on historic data
    """ calculates the parameters for the model based on historic data"""
    # load dataframe of past data for the predictive model
    df = rs.get_results(current_season_only=False)

    # set up the model
    modelFTAG = smf.ols(formula='FTAG ~ AST + ASO + AC', data=df)
    return modelFTAG.fit()

def exp_goals_predictor(fs, rs, ts):    # predicts expG from the savedd model
    """ calculates expG model and adds home and away expG to a list of games"""
    res_fthg = train_fthg_model(rs)
    res_ftag = train_ftag_model(rs)

    game_stats = prepare_combined_stats(fs, rs, ts)

    # Apply the model to a list of games
    fthg_pred = res_fthg.predict(game_stats)
    ftag_pred = res_ftag.predict(game_stats)

    game_stats["PredFTHG"] = fthg_pred
    game_stats["PredFTAG"] = ftag_pred
    
    return game_stats