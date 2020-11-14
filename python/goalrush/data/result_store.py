from .utils import format_df

class ResultStore:

    def __init__(self, results_df):
        self.results = results_df
        self.results['btts'] = (self.results['FTHG'] > 0) & (self.results['FTAG'] > 0)

    def get_results(self):
        return self.results

    def get_team_results(self, team_name, format="df"):
        values = self.results[(self.results['HomeTeam'] == team_name) | (self.results['AwayTeam'] == team_name)]
        return format_df(values, format)