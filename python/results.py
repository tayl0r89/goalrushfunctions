import requests
import pandas as pd
import io
from google.cloud import firestore
import datetime

PREMIER_LEAGUE = "E0.csv"
CHAMPIONSHIP = "E1.csv"
LEAGUE_ONE = "E2.csv"
LEAGUE_TWO = "E3.csv"
urlprefix = "https://www.football-data.co.uk/mmz4281/2021/"
db = firestore.Client()

def read(league):
    r = requests.post(urlprefix+league)
    if r.ok:
        data = r.content.decode('utf8')
        return pd.read_csv(io.StringIO(data))

def ingest(games):
    games_dict = games.to_dict(orient="index")
    batch = db.batch()
    for key, value in games_dict.items():
        id = value['Div'] + value['HomeTeam'] + value['AwayTeam']
        datestring = value['Date'] + value['Time']
        date = datetime.datetime.strptime(datestring, '%d/%m/%Y%H:%M')
        value['Date'] = date
        value.pop('Time', None)
        docRef = db.collection('results').document(id)
        docRef.set(value)
    batch.commit()

def process_league(league):
    results = read(league)
    ingest(results)

process_league(PREMIER_LEAGUE)
process_league(CHAMPIONSHIP)
process_league(LEAGUE_ONE)
process_league(LEAGUE_TWO)