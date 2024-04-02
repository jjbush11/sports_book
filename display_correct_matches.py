from db_connect_matches import ConnectDbMatch
from web_scraper import grab_nhl_moneylines, grab_nhl_scores

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
    # Get lists of winning and losing teams with scores
    teams_scores = grab_nhl_scores()
    print(teams_scores)
    # Separate
    winning_teams = teams_scores[0]
    losing_teams = teams_scores[1]
    winning_scores = teams_scores[2]
    losing_scores = teams_scores[3]

    # Get teams money lines
    teams_odds = grab_nhl_moneylines()
    print(teams_odds)
    # Separate
    away_teams = teams_odds[0]
    away_odds = teams_odds[1]
    home_teams = teams_odds[2]
    home_odds = teams_odds[3]
    datetimes = teams_odds[4]

    for i in range(0, len(winning_scores)):
        print(winning_teams[i])
        print(winning_scores[i])


upload_current_matches_and_moneyline_db()
