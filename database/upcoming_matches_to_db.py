import web_scraper
from db_upcoming_matches import ConnectDbMatch
from web_scraper import grab_scores, grab_moneylines

db_match = ConnectDbMatch()

def display_upcoming_matches():
    all_matches = db_match.get_all_matches()
    for match in all_matches:
        db_match.check_and_set_if_match_settled(match.id)
        print(match.id)
        if match.is_settled:
            print("Settled Game: " + match.team1 + " vs " + match.team2)
        elif not match.is_settled:
            print("Not settled Game: " + match.team1 + " vs " + match.team2)


def upload_current_matches_and_moneyline_db():

    # List of sport scores urls
    scores_links = [web_scraper.NBA_SCORES_URL, web_scraper.NHL_SCORES_URL,
                    web_scraper.MLB_SCORES_URL]
    # List of sport odds urls
    odds_links = [web_scraper.NBA_MONEYLINE_URL, web_scraper.NHL_MONEYLINE_URL,
                  web_scraper.MLB_MONEYLINE_URL]
    # Create db obj to connect to sport match up table
    db_match = ConnectDbMatch()

    # Loop through getting scores links
    for i in range(0, len(scores_links)):
        # Get lists of winning and losing teams with scores
        teams_scores = grab_scores(scores_links[i])

        # Separate into 4 different lists
        winning_teams = teams_scores[0]
        losing_teams = teams_scores[1]
        winning_scores = teams_scores[2]
        losing_scores = teams_scores[3]

        # Get odds
        teams_odds = grab_moneylines(odds_links[i])

        # Separate into 4 different lists
        away_teams = teams_odds[0]
        away_odds = teams_odds[2]
        home_teams = teams_odds[1]
        home_odds = teams_odds[3]
        datetimes = teams_odds[4]

        for j in range(0, len(away_odds)):
            print('')
            # print(winning_teams[j] + ': ' + str(winning_scores[j]))
            # print(losing_teams[j] + ': '+ str(losing_scores[j]))

            print(away_teams[j] + '(' + str(away_odds[j])+')')
            print(str(home_teams[j]) + '(' + str(home_odds[j])+')')
            print(datetimes[j]) # need to format date to fit correctly

        for j in range(0, len(winning_teams)):
            pass
            # upload home team and score
            # upload away team and score




upload_current_matches_and_moneyline_db()
  