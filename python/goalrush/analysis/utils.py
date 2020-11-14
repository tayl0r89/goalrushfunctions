def recent_home_games(df, team_name, n):
    # produces a df with last n home games for a given team
    # needs a df with date, team and number of games
    """ produces a df with last n home games for a given team """
    results = df.sort_values(by="Date", ascending=False)
    return results.loc[results["HomeTeam"]==team_name].head(n)

def recent_away_games(df, team_name, n):
    # produces a df with last n away games for a given team
    # needs a df with date, team and number of games
    """ produces a df with last n away games for a given team """
    results = df.sort_values(by="Date", ascending=False)
    return results.loc[results["AwayTeam"]==team_name].head(n)
