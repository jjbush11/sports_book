import requests
from bs4 import BeautifulSoup
from datetime import datetime


# Scores URLs
NBA_SCORES_URL = (f'https://www.basketball-reference.com/boxscores/'
           f'?year={datetime.now().year}&month={datetime.now().month}&day={datetime.now().day - 1}')
NHL_SCORES_URL = (f'https://www.hockey-reference.com/boxscores/'
           f'?year={datetime.now().year}&month={datetime.now().month}&day={datetime.now().day - 1}')
MLB_SCORES_URL = (f'https://www.baseball-reference.com/boxes/'
           f'?year={datetime.now().year}&month={datetime.now().month}&day={datetime.now().day - 1}')

# Moneyline URLs
NBA_MONEYLINE_URL = ("https://vegas-odds.com/nba/odds/")
NHL_MONEYLINE_URL = ("https://vegas-odds.com/nhl/odds/")
MLB_MONEYLINE_URL = ("https://vegas-odds.com/mlb/odds/")

# Teams
mlb_teams = {
    "Arizona": "Arizona Diamondbacks",
    "Atlanta": "Atlanta Braves",
    "Baltimore": "Baltimore Orioles",
    "Boston": "Boston Red Sox",
    "Chicago Cubs": "Chicago Cubs",
    "Chicago White Sox": "Chicago White Sox",
    "Cincinnati": "Cincinnati Reds",
    "Cleveland": "Cleveland Guardians",
    "Colorado": "Colorado Rockies",
    "Detroit": "Detroit Tigers",
    "Houston": "Houston Astros",
    "Kansas City": "Kansas City Royals",
    "Los Angeles Angels": "Los Angeles Angels",
    "Los Angeles Dodgers": "Los Angeles Dodgers",
    "Miami": "Miami Marlins",
    "Milwaukee": "Milwaukee Brewers",
    "Minnesota": "Minnesota Twins",
    "New York Mets": "New York Mets",
    "New York Yankees": "New York Yankees",
    "Oakland": "Oakland Athletics",
    "Philadelphia": "Philadelphia Phillies",
    "Pittsburgh": "Pittsburgh Pirates",
    "San Diego": "San Diego Padres",
    "San Francisco": "San Francisco Giants",
    "Seattle": "Seattle Mariners",
    "St. Louis": "St. Louis Cardinals",
    "Tampa Bay": "Tampa Bay Rays",
    "Texas": "Texas Rangers",
    "Toronto": "Toronto Blue Jays",
    "Washington": "Washington Nationals"
}

nba_teams = {
    "Atlanta": "Atlanta Hawks",
    "Boston": "Boston Celtics",
    "Brooklyn": "Brooklyn Nets",
    "Charlotte": "Charlotte Hornets",
    "Chicago": "Chicago Bulls",
    "Cleveland": "Cleveland Cavaliers",
    "Dallas": "Dallas Mavericks",
    "Denver": "Denver Nuggets",
    "Detroit": "Detroit Pistons",
    "Golden State": "Golden State Warriors",
    "Houston": "Houston Rockets",
    "Indiana": "Indiana Pacers",
    "LA Clippers": "LA Clippers",
    "LA Lakers": "Los Angeles Lakers",
    "Memphis": "Memphis Grizzlies",
    "Miami": "Miami Heat",
    "Milwaukee": "Milwaukee Bucks",
    "Minnesota": "Minnesota Timberwolves",
    "New Orleans": "New Orleans Pelicans",
    "New York": "New York Knicks",
    "Oklahoma City": "Oklahoma City Thunder",
    "Orlando": "Orlando Magic",
    "Philadelphia": "Philadelphia 76ers",
    "Phoenix": "Phoenix Suns",
    "Portland": "Portland Trail Blazers",
    "Sacramento": "Sacramento Kings",
    "San Antonio": "San Antonio Spurs",
    "Toronto": "Toronto Raptors",
    "Utah": "Utah Jazz",
    "Washington": "Washington Wizards"
}
nhl_teams = {
    "Anaheim": "Anaheim Ducks",
    "Arizona": "Arizona Coyotes",
    "Boston": "Boston Bruins",
    "Buffalo": "Buffalo Sabres",
    "Calgary": "Calgary Flames",
    "Carolina": "Carolina Hurricanes",
    "Chicago": "Chicago Blackhawks",
    "Colorado": "Colorado Avalanche",
    "Columbus": "Columbus Blue Jackets",
    "Dallas": "Dallas Stars",
    "Detroit": "Detroit Red Wings",
    "Edmonton": "Edmonton Oilers",
    "Florida": "Florida Panthers",
    "Los Angeles": "Los Angeles Kings",
    "Minnesota": "Minnesota Wild",
    "Montreal": "Montreal Canadiens",
    "Nashville": "Nashville Predators",
    "New Jersey": "New Jersey Devils",
    "NY Islanders": "New York Islanders",
    "NY Rangers": "New York Rangers",
    "Ottawa": "Ottawa Senators",
    "Philadelphia": "Philadelphia Flyers",
    "Pittsburgh": "Pittsburgh Penguins",
    "San Jose": "San Jose Sharks",
    "Seattle": "Seattle Kraken",
    "St. Louis": "St. Louis Blues",
    "Tampa Bay": "Tampa Bay Lightning",
    "Toronto": "Toronto Maple Leafs",
    "Vancouver": "Vancouver Canucks",
    "Vegas": "Vegas Golden Knights",
    "Washington": "Washington Capitals",
    "Winnipeg": "Winnipeg Jets"
}


def main() -> int:
    return 0


# Scrape nhl web scores
def grab_scores(url: str) -> [[]]:
    # Request scores page & build soup
    scores_page = requests.get(url)
    soup = BeautifulSoup(scores_page.content, "html.parser")

    # Lists for winning, losing teams & scores
    away_teams = list()
    home_teams = list()
    away_scores = list()
    home_scores = list()

    # Score sections at the top of the page, still needs parsing
    if url == NBA_SCORES_URL:
        if len(soup.find_all("div", class_="game_summaries")) > 0:
            scores_divs = soup.find_all("div", class_="game_summaries")[0].find_all("div", class_="game_summary expanded nohover")
        else:
            return [[]]
    else:
        if len(soup.find_all("div", class_="game_summary nohover")) > 0:
            scores_divs = soup.find_all("div", class_="game_summary nohover")
        else:
            return [[]]

    for div in scores_divs:
        # Game loser, winner data
        away_team = div.find("table").find("tbody").find_all("tr")[0].find_all("td")
        home_team = div.find("table").find("tbody").find_all("tr")[1].find_all("td")

        # Get team names
        away_team_name = str(away_team[0].find("a").get_text())
        home_team_name = str(home_team[0].find("a").get_text())

        # Gets all the team names in the same format so that the database ID is consistent
        if url == NBA_SCORES_URL:
            for key, value in nba_teams.items():
                if key.lower() in away_team_name.lower():
                    away_team_name = value
                if key.lower() in home_team_name.lower():
                    home_team_name = value
        elif url == NHL_SCORES_URL:
            for key, value in nhl_teams.items():
                if key.lower() in away_team_name.lower():
                    away_team_name = value
                if key.lower() in home_team_name.lower():
                    home_team_name = value
        elif url == MLB_SCORES_URL:
            for key, value in mlb_teams.items():
                if key.lower() in away_team_name.lower():
                    away_team_name = value
                if key.lower() in home_team_name.lower():
                    home_team_name = value

        # Append team names
        away_teams.append(away_team_name)
        home_teams.append(home_team_name)

        # Append scores
        away_scores.append(int(away_team[1].get_text()))
        home_scores.append(int(home_team[1].get_text()))

    return_list = list()
    return_list.append(away_teams)
    return_list.append(home_teams)
    return_list.append(away_scores)
    return_list.append(home_scores)
    return return_list


def grab_moneylines(url: str) -> [[]]:
    # Create soup, find table bodies containing odds, tables
    moneyline_page = requests.get(url)
    soup = BeautifulSoup(moneyline_page.content, "html.parser")

    # Get the moneyline listings. If none exist, return an empty nested list
    moneyline_entries = soup.find_all("div", class_="table-responsive oddstablev2")[0].find("table").find_all("tbody")
    if len(moneyline_entries) < 1:
        return [[]]

    away_teams = list()
    away_odds = list()
    home_teams = list()
    home_odds = list()
    datetimes = list()

    for entry in moneyline_entries:
        # Find home & away entries containing team names, odds
        away_entry = entry.find_all("tr")[0]
        home_entry = entry.find_all("tr")[1]

        # Get team names
        away_team_name = str(away_entry.find("th").get_text())
        home_team_name = str(home_entry.find("th").get_text())

        # Gets all the team names in the same format so that the database ID is consistent
        if url == NBA_MONEYLINE_URL:
            for key, value in nba_teams.items():
                if key.lower() in away_team_name.lower():
                    away_team_name = value
                if key.lower() in home_team_name.lower():
                    home_team_name = value
        elif url == NHL_MONEYLINE_URL:
            for key, value in nhl_teams.items():
                if key.lower() in away_team_name.lower():
                    away_team_name = value
                if key.lower() in home_team_name.lower():
                    home_team_name = value
        elif url == MLB_MONEYLINE_URL:
            for key, value in mlb_teams.items():
                if key.lower() in away_team_name.lower():
                    away_team_name = value
                if key.lower() in home_team_name.lower():
                    home_team_name = value

        # Get team name text
        away_teams.append(away_team_name)
        home_teams.append(home_team_name)

        # Get odds
        try:
            away_odds.append(int(away_entry.find("td").get_text()))
        except ValueError:
            away_odds.append(0)
        try:
            home_odds.append(int(home_entry.find("td").get_text()))
        except ValueError:
            home_odds.append(0)

         # Get datetime
        datetimes.append(away_entry.find_all("td")[3].get_text())

    # Create and append lists to return list
    return_list = list()
    return_list.append(away_teams)
    return_list.append(home_teams)
    return_list.append(away_odds)
    return_list.append(home_odds)
    return_list.append(datetimes)
    return return_list


if __name__ == "__main__":
    main()