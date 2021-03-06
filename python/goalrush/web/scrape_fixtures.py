# import HTMLSession from requests_html
from requests_html import HTMLSession

# import BeautifulSoup
from bs4 import BeautifulSoup
import requests

import pandas as pd
import datetime

def get_fixtures():   #function to prepare goal rush fixtures
    """This function prepares a csv file with the weeks fixtures"""
    # create a HTML Session object
    session = HTMLSession()

    # use the object above to connect to the needed webpage
    resp = session.get("https://www.footballpools.com/pool-games/goal-rush")

    # run JavaScript code on webpage
    resp.html.render()
    #print(resp.html.html)

    # create beautiful soup object
    soup = BeautifulSoup(resp.html.html, "html.parser")

    gameweek_date_elements = soup.select("span.date")
    if len(gameweek_date_elements) > 0:
        datestr = gameweek_date_elements[0].get_text()
        gameweek_date = datetime.datetime.strptime(datestr, '%d %b @ %H:%M')
        gameweek_date = gameweek_date.replace(year=datetime.datetime.now().year)

    # create an empty list for the games
    games_list = []

    for item in soup.select("div.goal_rush_8"):
        #print("------------------------")
        # for each game we need div.number, div.home and div.away
        
        number = item.select("div.number")
        if len(number) > 0:
            #print(number[0].get_text())
            no = number[0].get_text()

        home = item.select("div.home")
        if len(home) > 0:
            #print(home[0].get_text())
            home_team = home[0].get_text()

        away = item.select("div.away")
        if len(away) > 0:
            #print(away[0].get_text())
            away_team = away[0].get_text()

        games_list.append({
            'number' : no,
            'home' : home_team, 
            'away' : away_team,
            'gameweekDate' : gameweek_date
        })
    
    return pd.DataFrame(games_list)