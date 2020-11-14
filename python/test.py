from goalrush.data.scraping_fixture_store import ScrapingFixtureStore
from goalrush.data.csv_team_store import CsvTeamStore
from goalrush.data.url_result_store import UrlResultStore
from goalrush.web.download_results import download_results
from goalrush.analysis.game_projections import game_projections

fs = ScrapingFixtureStore()
ts = CsvTeamStore("C:\\Users\\ste\\dev\\teamdata.csv")
rs = UrlResultStore()

print(game_projections(fs, rs, ts))
