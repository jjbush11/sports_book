import web_scraper
from db_upcoming_matches import ConnectDbUpcomingMatch

# Constant definitions
AWAY_TEAM_COL = 0
HOME_TEAM_COL = 1
AWAY_ODDS_COL = 2
HOME_ODDS_COL = 3
DATETIME_COL = 4

MONTH = 0
DAY = 1
TIME = 3


# Main: upload nhl scores
def main() -> None:
    upload_current_matches()


# Upload current matches
def upload_current_matches() -> None:
    # Grab the matchups nested list, and connect to database.
    nhl_scores = web_scraper.grab_moneylines(web_scraper.NHL_MONEYLINE_URL)
    db = ConnectDbUpcomingMatch()
    db.remove_all()

    for game in range(len(nhl_scores[0])):
        # Get individual game fields
        away_team = nhl_scores[AWAY_TEAM_COL][game]
        home_team = nhl_scores[HOME_TEAM_COL][game]
        away_odds = nhl_scores[AWAY_ODDS_COL][game]
        home_odds = nhl_scores[HOME_ODDS_COL][game]
        datetime = nhl_scores[DATETIME_COL][game]
        datetime_split = datetime.split(" ")
        month_and_day = datetime_split[MONTH] + " " + datetime_split[DAY]
        time = datetime_split[TIME]

        # Print games, and upload them to the database
        print(away_team, ": ", away_odds, " ", home_team, ": ", home_odds, " @", month_and_day, ", ", time)
        new_upcoming = db.add_new_upcoming_match(
            id=f'{away_team}{home_team}{datetime}',
            home=home_team,
            home_odds=home_odds,
            away=away_team,
            away_odds=away_odds,
            date=month_and_day,
            time=time
        )


# Run main: upload NHL scores
if __name__ == "__main__":
    main()
