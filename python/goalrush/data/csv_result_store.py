from .result_store import ResultStore
import pandas as pd

class CsvResultStore(ResultStore):

    def __init__(self, csv_files):
        df = pd.concat(list(map(pd.read_csv, csv_files)))
        super().__init__(df)
