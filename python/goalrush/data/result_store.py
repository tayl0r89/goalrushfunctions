from .utils import format_df

current_season="2021"

class ResultStore:

    def __init__(self, results_df):
        self.results = results_df
        self.results['btts'] = (self.results['FTHG'] > 0) & (self.results['FTAG'] > 0)
        self.results["HSO"] = self.results["HS"] - self.results["HST"]
        self.results["ASO"] = self.results["AS"] - self.results["AST"]
        self.results['season'] = self.results['season'].astype(str)

    def get_results(self, current_season_only=True):
        if current_season_only:
            return self.results[self.results['season'] == current_season]
        return self.results

    def get_team_results(self, team_name, format="df"):
        values = self.results[(self.results['HomeTeam'] == team_name) | (self.results['AwayTeam'] == team_name)]
        return format_df(values, format)