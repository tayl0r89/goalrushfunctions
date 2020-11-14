from .btts_form import btts_away_form, btts_home_form

def goal_rush_rating(rs, fs, ts):    # runs form table for the goal rush fixtures
    """ runs form table for the goal rush fixtures"""

    # prepare goal rush fixture list from pools website
    fixtures = fs.get_fixtures()
    fixtures['HomeId'] = fixtures['home'].apply(ts.get_team_id)
    fixtures['AwayId'] = fixtures['away'].apply(ts.get_team_id)
    fixtures = fixtures[['number', 'HomeId', 'home', 'AwayId', 'away']].dropna()

    # look up BTTS home and away form
    home_btts_form = btts_home_form(rs)
    away_btts_form = btts_away_form(rs)
    home_btts_form['HomeId'] = home_btts_form['HomeTeam'].apply(ts.get_team_id)
    away_btts_form['AwayId'] = away_btts_form['AwayTeam'].apply(ts.get_team_id)

    # merge home and away btts form onto the fixtures
    fixtures_home_data = fixtures.merge(home_btts_form, on = 'HomeId')
    fixtures_data = fixtures_home_data.merge(away_btts_form, on = 'AwayId')

    # remove columns that aren't required
    fixtures_data = fixtures_data[['number', 'HomeId', 'home', 'AwayId', 'away', 'HBTTS', 'ABTTS']]
    fixtures_data['Rating'] = fixtures_data.HBTTS + fixtures_data.ABTTS

    # sort by rating
    return fixtures_data.sort_values(by="Rating", ascending=False)