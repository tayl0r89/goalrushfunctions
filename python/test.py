from goalrush.data.scraping_fixture_store import ScrapingFixtureStore
from goalrush.data.csv_team_store import CsvTeamStore
from goalrush.data.url_result_store import UrlResultStore
from goalrush.web.download_results import download_results
from goalrush.analysis.goal_rush_rating import goal_rush_rating

fs = ScrapingFixtureStore()
ts = CsvTeamStore("C:\\Users\\ste\\dev\\teamdata.csv")
rs = UrlResultStore()

print(goal_rush_rating(rs, fs, ts))
