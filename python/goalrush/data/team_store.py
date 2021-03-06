from .utils import format_df

class TeamStore:
    """This is an abstract version of the TeamStore"""
    def __init__(self, df):
        self.df = df

    def get_teams(self, format="df"):
        """Get a list of all teams allowing for a specific format"""
        return format_df(self.df, format)

    def get_team(self, team_name):
        """Retrieves a single team dict first looking at team name, then aliases."""
        lookup = lambda row: (row['name'] == team_name) | (team_name in row['aliases'])
        temp = self.df[self.df.apply(lookup, axis = 1)]
        response = list(temp.to_dict(orient="index").values())
        return response[0] if len(response) > 0 else None
    
    def get_team_id(self, team_name):
        """Returns the id for a given team, or None if the team is not found"""
        team = self.get_team(team_name)
        return team['id'] if not team is None else None
        