from .result_store import ResultStore
from .utils import get_cached
from ..web.download_results import download_results

seasons = ["2021", "1920", "1819", "1718", "1617"]

class UrlResultStore(ResultStore):

    def __init__(self):
        super().__init__(get_cached("results", lambda: download_results(seasons)))