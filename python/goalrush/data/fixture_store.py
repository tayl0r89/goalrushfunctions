class FixtureStore:

    def __init__(self, df):
        self.fixtures = df

    def get_fixtures(self):
        return self.fixtures.sort_values('number')