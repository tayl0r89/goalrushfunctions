import requests
import io
import pandas as pd

football_data_url = "https://www.football-data.co.uk/mmz4281/{season}/{league}"
files = ["E0.csv", "E1.csv", "E2.csv", "E3.csv"]
current_season = "2021"

def download_results(season=current_season):
    frames = list(map(lambda x: download_results_league(x, season), files))
    return pd.concat(frames)

def download_results_league(league, season=current_season):
    print("Downloading {url}".format(url=get_url(league, season)))
    r = requests.get(get_url(league, season))
    if r.ok:
        data = r.content.decode("utf8")
        return pd.read_csv(io.StringIO(data))

def get_url(league, season=current_season):
    return football_data_url.format(season=season, league=league)