from goalrush.data.scraping_fixture_store import ScrapingFixtureStore
from goalrush.data.csv_team_store import CsvTeamStore
from goalrush.data.csv_result_store import CsvResultStore
from goalrush.analysis.fixture_summary import fixture_summaries

fs = ScrapingFixtureStore()
ts = CsvTeamStore("C:\\Users\\ste\\dev\\teamdata.csv")
rs = CsvResultStore([
    "C:\\Users\\ste\\dev\\E0.csv",
    "C:\\Users\\ste\\dev\\E1.csv",
    "C:\\Users\\ste\\dev\\E2.csv",
    "C:\\Users\\ste\\dev\\E3.csv",
])

print(fixture_summaries(fs, ts, rs))
