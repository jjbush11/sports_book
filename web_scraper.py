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


def main() -> int:
    print(grab_scores(NHL_SCORES_URL))
    print(grab_moneylines(NHL_MONEYLINE_URL))
    return 0


# Scrape nhl web scores
def grab_scores(url: str) -> [[]]:
    # Request scores page & build soup
    scores_page = requests.get(url)
    soup = BeautifulSoup(scores_page.content, "html.parser")

    # Lists for winning, losing teams & scores
    winning_teams = list()
    losing_teams = list()
    winning_scores = list()
    losing_scores = list()

    # Score sections at the top of the page, still needs parsing
    scores_divs = soup.find_all("div", class_="game_summary nohover")
    for div in scores_divs:
        # Game loser, winner data
        game_loser = div.find("table").find("tbody").find_all(class_="loser")[0].find_all("td")
        game_winner = div.find("table").find("tbody").find_all(class_="winner")[0].find_all("td")

        # Append team names
        losing_teams.append(game_loser[0].find("a").get_text())
        winning_teams.append(game_winner[0].find("a").get_text())

        # Append scores
        losing_scores.append(int(game_loser[1].get_text()))
        winning_scores.append(int(game_winner[1].get_text()))

    return_list = list()
    return_list.append(winning_teams)
    return_list.append(losing_teams)
    return_list.append(winning_scores)
    return_list.append(losing_scores)
    return return_list


def grab_moneylines(url: str) -> [[]]:
    # Create soup, find table bodies containing odds, tables
    moneyline_page = requests.get(url)
    soup = BeautifulSoup(moneyline_page.content, "html.parser")
    moneyline_entries = soup.find_all("div", class_="table-responsive oddstablev2")[0].find("table").find_all("tbody")[1:]
    away_teams = list()
    away_odds = list()
    home_teams = list()
    home_odds = list()
    datetimes = list()

    for entry in moneyline_entries:
        # Find home & away entries containing team names, odds
        away_entry = entry.find_all("tr")[0]
        home_entry = entry.find_all("tr")[1]

        # Get team name text
        away_teams.append(away_entry.find("th").get_text())
        home_teams.append(home_entry.find("th").get_text())

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
