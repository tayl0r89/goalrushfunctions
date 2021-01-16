from goalrush.data.scraping_fixture_store import ScrapingFixtureStore
from goalrush.data.csv_team_store import CsvTeamStore
from goalrush.data.url_result_store import UrlResultStore
from goalrush.web.download_results import download_results
from goalrush.analysis.fixture_summary import fixture_summaries

from google.cloud import firestore

fs = ScrapingFixtureStore()
ts = CsvTeamStore("C:\\Users\\ste\\dev\\teamdata.csv")
rs = UrlResultStore()

db = firestore.Client()

def get_fixture_ref(fixture):
    return "summary-{number}-{date}".format(number=fixture['number'], date=fixture['gameweekDate'])

batch = db.batch()

for s in fixture_summaries(fs, ts, rs):
    ref = db.collection('fixtureSummaries').document(get_fixture_ref(s['fixture']))
    batch.set(ref, s)

batch.commit()