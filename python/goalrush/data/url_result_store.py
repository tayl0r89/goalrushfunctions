from .result_store import ResultStore
from .utils import get_cached
from ..web.download_results import download_results

class UrlResultStore(ResultStore):

    def __init__(self):
        super().__init__(get_cached("results", download_results))