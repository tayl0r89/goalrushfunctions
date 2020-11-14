from .team_stats import prepare_combined_stats
from .shot_model import exp_goals_predictor
from .poisson_calcs import *

def game_projections(fs, rs, ts):    # calculates game outcome probebilities for a set of fixtures
    """ calculates game outcome probebilities for a set of fixtures"""

    # calculate FTHG & FTAG for teams in the fixtures
    games_stats = exp_goals_predictor(fs, rs, ts)

    # add columns to games for each outcome type
    games_stats["Home win"] = games_stats.apply(lambda x: home_win_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["Away win"] = games_stats.apply(lambda x: away_win_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["Draw"] = games_stats.apply(lambda x: draw_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["Score draw"] = games_stats.apply(lambda x: score_draw_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["BTTS"] = games_stats.apply(lambda x: btts_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["U2.5 goals"] = games_stats.apply(lambda x: under_x_goals_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["Home win to nil"] = games_stats.apply(lambda x: home_win_to_nil_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["Away win to nil"] = games_stats.apply(lambda x: away_win_to_nil_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["Home win BTTS"] = games_stats.apply(lambda x: home_win_btts_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)
    games_stats["Away win BTTS"] = games_stats.apply(lambda x: away_win_btts_probability(x['PredFTHG'], x['PredFTAG']), axis = 1)

    return games_stats.loc[:, ['HomeId', 'HomeTeam', 'AwayId', 'AwayTeam', 'Home win', 'Draw', 'Away win', 'Score draw', 'BTTS', 'U2.5 goals', 'Home win to nil', 'Away win to nil', 'Home win BTTS', 'Away win BTTS']]
