from goalrush.data.scraping_fixture_store import ScrapingFixtureStore
from goalrush.data.csv_team_store import CsvTeamStore
from goalrush.data.url_result_store import UrlResultStore
from goalrush.analysis.fixture_summary import fixture_summaries
from goalrush.web.download_results import download_results

fs = ScrapingFixtureStore()
ts = CsvTeamStore("C:\\Users\\ste\\dev\\teamdata.csv")
rs = UrlResultStore()

print(fixture_summaries(fs, ts, rs))
