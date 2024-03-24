import requests
from bs4 import BeautifulSoup

# Constant definitions
NHL_URL = 'https://www.hockey-reference.com/boxscores/?year=2024&month=03&day=22'


# Main: scrape NHL web scores
def main() -> int:
    # Request scores page & build soup
    nhl_scores_page = requests.get(NHL_URL)
    soup = BeautifulSoup(nhl_scores_page.content, "html.parser")

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

    return 0

if __name__ == "__main__":
    main()
