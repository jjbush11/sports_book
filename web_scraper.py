import requests
from bs4 import BeautifulSoup

# Constant definitions
NHL_URL = 'https://www.hockey-reference.com/boxscores/?year=2024&month=03&day=22'


# Main: scrape NHL web scores
def main() -> int:
    # Request scores page & build soup
    nhl_scores_page = requests.get(NHL_URL)
    soup = BeautifulSoup(nhl_scores_page.content, "html.parser")

    scores_divs = soup.find_all("div", class_="game_summary nohover")
    for div in scores_divs:
        print(div, "\n")



if __name__ == "__main__":
    main()
