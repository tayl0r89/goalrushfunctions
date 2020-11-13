import pandas as pd
from .team_store import TeamStore
from .utils import combine_rows

class CsvTeamStore(TeamStore):

    def __init__(self, csv_file):
        temp = pd.read_csv(csv_file, header=0, names=["id", "name", "alias1", "alias2", "alias3"])
        temp['aliases'] = temp.apply(combine_rows, axis=1)
        super().__init__(temp[['id','name','aliases']])

