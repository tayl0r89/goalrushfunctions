from google.cloud import firestore
import pandas as pd

def results_to_arr(results):
    data = []
    for result in results:
        data.append(result.to_dict())
    return data

def results_to_df(results):
    return pd.DataFrame(results_to_arr(results))

class DataStore:

    def __init__(self):
        self.db = firestore.Client()
    
    def get_results(self):
        if not hasattr(self, 'results'):
            temp = self.db.collection("results").stream()
            self.results = results_to_df(temp).sort_values("Date", ascending=False)
            self.results['btts'] = (self.results['FTHG'] > 0) & (self.results['FTAG'] > 0)
        return self.results
    
    def get_fixtures(self):
        if not hasattr(self, 'fixtures'):
            temp = self.db.collection("fixtures").stream()
            self.fixtures = results_to_df(temp).sort_values('number')
        return self.fixtures
    
    def get_fixtures_arr(self):
        fixtures_dict = self.get_fixtures().to_dict(orient="index")
        return list(fixtures_dict.values())

    def get_teams(self):
        if not hasattr(self, 'teams'):
            temp = self.db.collection("teams").stream()
            self.teams = results_to_df(temp)
        return self.teams

    def get_team(self, team_name):
        teams = self.get_teams()
        lookup = lambda row: (row['name'] == team_name) | (team_name in row['aliases'])
        temp = teams[teams.apply(lookup, axis = 1)]
        response = list(temp.to_dict(orient="index").values())
        return response[0] if len(response) > 0 else None
    
    def get_team_results(self, team_name):
        results = self.get_results()
        return results[(results['HomeTeam'] == team_name) | (results['AwayTeam'] == team_name)]

# def get_fixture(fixture_id):
#     fixture = db.collection("fixtures").document(fixture_id).get()
#     if fixture.exists:
#         return fixture.to_dict()
#     return None

def fixture_summary(fixture, ds):
    home_team = ds.get_team(fixture['home'])
    away_team = ds.get_team(fixture['away'])
    summary = {}
    summary['fixture'] = fixture
    if not home_team is None:
        home_team_name = home_team['name']
        home_team_results = ds.get_team_results(home_team_name)
        home_team_btts = home_team_results['btts'][0:6].tolist()
        home_team_home_btts = home_team_results[home_team_results['HomeTeam'] == home_team_name]['btts'][0:6].tolist()
        summary['homeTeamBTTS'] = home_team_btts
        summary['homeTeamHomeBTTS'] = home_team_home_btts
    
    if not away_team is None:
        away_team_name = away_team['name']
        away_team_results = ds.get_team_results(away_team_name)
        away_team_btts = away_team_results['btts'][0:6].tolist()
        away_team_away_btts = away_team_results[away_team_results['AwayTeam'] == away_team_name]['btts'][0:6].tolist()
        summary['awayTeamBTTS'] = away_team_btts
        summary['awayTeamAwayBTTS'] = away_team_away_btts
    
    return summary

def handle_summary_request(request):
    ds = DataStore()
    result = {}
    result['summaries'] = list(map(lambda fix: fixture_summary(fix, ds), ds.get_fixtures_arr()))
    return result
