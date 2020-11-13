from .fixture_store import FixtureStore
from ..web.scrape_fixtures import get_fixtures
from .utils import get_cached
import pandas as pd

class ScrapingFixtureStore(FixtureStore):

    def __init__(self):
        super().__init__(get_cached("fixtures", get_fixtures))
