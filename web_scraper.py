import requests
from bs4 import BeautifulSoup

# Constant definitions
NHL_URL = 'https://www.nhl.com/scores/2024-03-22'


# Main: scrape NHL web scores
def main() -> int:
    # Request scores page & build soup
    nhl_scores_page = requests.get(NHL_URL)
    soup = BeautifulSoup(nhl_scores_page.content, "html.parser")

    scores_divs = soup.find_all("div")
    for score in scores_divs:
        print(score, "\n")


if __name__ == "__main__":
    main()
