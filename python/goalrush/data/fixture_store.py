from .utils import format_df

class FixtureStore:

    def __init__(self, df):
        self.fixtures = df

    def get_fixtures(self, format="df"):
        return format_df(self.fixtures.sort_values('number'), format=format)