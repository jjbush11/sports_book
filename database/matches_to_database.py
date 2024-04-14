import web_scraper
import datetime
from db_upcoming_matches import ConnectDbUpcomingMatch
from db_settled_matches import ConnectDbSettledMatch

# Constant definitions
AWAY_TEAM_COL = 0
HOME_TEAM_COL = 1
AWAY_ODDS_COL = 2
HOME_ODDS_COL = 3
DATETIME_COL = 4

HOME_SCORES_COL = 2
AWAY_SCORES_COL = 3

MONTH = 0
DAY = 1
TIME = 3

MONTHS_INDEX = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


# Main: upload scores
def main() -> None:
    upload_current_matches()
    upload_settled_matches()


# Upload current matches
def upload_current_matches() -> None:
    # Upload grabbed games to odds db
    def scores_helper(games_list: [[]], length: int, sport: str):
        for game in range(length):
            # Get individual game fields
            away_team = games_list[AWAY_TEAM_COL][game]
            home_team = games_list[HOME_TEAM_COL][game]
            away_odds = games_list[AWAY_ODDS_COL][game]
            home_odds = games_list[HOME_ODDS_COL][game]
            date_time = games_list[DATETIME_COL][game]
            datetime_split = date_time.split(" ")
            month_and_day = datetime_split[MONTH] + " " + datetime_split[DAY]
            time = datetime_split[TIME]

            # Print games, and upload them to the database
            print(away_team, ": ", away_odds, " ", home_team, ": ", home_odds, " @", month_and_day, ", ", time)
            new_upcoming = db.add_new_upcoming_match(
                id=f'{away_team}{home_team}{month_and_day}',
                home=home_team,
                home_odds=home_odds,
                away=away_team,
                away_odds=away_odds,
                date=month_and_day,
                time=time,
                sport=sport
            )

    # Grab the matchups nested list, and connect to database.
    nhl_odds = web_scraper.grab_moneylines(web_scraper.NHL_MONEYLINE_URL)
    mlb_odds = web_scraper.grab_moneylines(web_scraper.MLB_MONEYLINE_URL)
    nba_odds = web_scraper.grab_moneylines(web_scraper.NBA_MONEYLINE_URL)
    db = ConnectDbUpcomingMatch()
    db.remove_all()

    # Upload games and odds to database
    scores_helper(nhl_odds, len(nhl_odds[0]), "NHL")
    scores_helper(mlb_odds, len(mlb_odds[0]), "MLB")
    scores_helper(nba_odds, len(nba_odds[0]), "NBA")


# Upload yesterday's matches to the database with scores
def upload_settled_matches():
    # Handle the scores upload loops
    def scores_helper(games_list: [[]], length: int, sport: str):
        for game in range(length):
            # Get individual game fields
            home_team = games_list[HOME_TEAM_COL][game]
            road_team = games_list[AWAY_TEAM_COL][game]
            road_score = games_list[HOME_SCORES_COL][game]
            home_score = games_list[AWAY_SCORES_COL][game]
            current_time = datetime.datetime.now()
            month = MONTHS_INDEX[current_time.month - 1]
            day = current_time.day - 1
            date = month + " " + str(day)

            # Print games, and upload them to the database
            print(road_team, ": ", road_score, " ", home_team, ": ", home_score)
            new_settled = db.add_new_settled_match(
                par_id=f'{home_team}{road_team}{date}',
                away=road_team,
                away_score=road_score,
                home=home_team,
                home_score=home_score,
                sport=f'{sport}'
            )

    # Get scores, connect to database
    nhl_scores = web_scraper.grab_scores(web_scraper.NHL_SCORES_URL)
    mlb_scores = web_scraper.grab_scores(web_scraper.MLB_SCORES_URL)
    nba_scores = web_scraper.grab_scores(web_scraper.NBA_SCORES_URL)
    db = ConnectDbSettledMatch()

    # Upload these scores
    scores_helper(nhl_scores, len(nhl_scores[0]), "NHL")
    scores_helper(mlb_scores, len(mlb_scores[0]), "MLB")
    scores_helper(nba_scores, len(nba_scores[0]), "NBA")


# Run main: upload NHL scores
if __name__ == "__main__":
    main()
