# Logon behavior functions file
from database.db_connect_user import ConnectDbUser
from database import web_scraper
from database import matches_to_database
from database.db_bet import ConnectDbBet
from database.db_settled_matches import ConnectDbSettledMatch
from database.db_connect_user import ConnectDbUser
import datetime


# Check the user's balance. Set it to $5 if it is less than $5.
def check_balance(username: str) -> None:
    user = ConnectDbUser()
    user_balance = user.get_row_by_user(username).balance

    if user_balance < 5:
        user.edit_row(username, "balance", 5)


# On startup: update the current matchups
def update_tables() -> None:
    matches_to_database.main()


def check_if_settled_and_pay(username: str) -> None:
    # For all user bets that are not paid out:
    # Check if match ID is in settled matches:
    # If it's there, and mark the bet as settled and pay out if they won.

    # Connect to databases
    db_bets = ConnectDbBet()
    db_settled_matches = ConnectDbSettledMatch()
    db_user = ConnectDbUser()

    # Get all bets by user
    user_bets = db_bets.get_all_active_bets_by_user(username)

    for bet in user_bets:
        # Initialize vars
        win = -1
        user = db_user.get_row_by_user(username)

        # Check if game related to the bet is settled
        match_bet_on = db_settled_matches.get_settled_matches_by_id(bet.id)
        # If bet is settled
        if match_bet_on is not None:
            # Set settled to true
            db_bets.edit_bet_row(bet.id, username,'settled', 1)

            # Check if bet was won
            team_bet_on = bet.team

            # If the team bet on was away team
            if team_bet_on == match_bet_on.away:
                # Check if away score is higher than home score
                if match_bet_on.away_score > match_bet_on.home_score:
                    win = 1
                else:
                    win = 0
            # If team bet on was the home team
            elif team_bet_on == match_bet_on.home:
                # Check if home score is higher than away score
                if match_bet_on.home_score > match_bet_on.away_score:
                    win = 1
                else:
                    win = 0

            # If bet won update balance
            print(win)
            if win:
                print("Updating balance")
                current_balance = user.balance
                new_balance = current_balance + bet.return_val

                # Set new balance
                db_user.edit_row(username, 'balance', new_balance)

            # Update win and is_payed flags
            db_bets.edit_bet_row(bet.id, username,'win', win)
            db_bets.edit_bet_row(bet.id, username,'is_payed', 1)


# Check the current time. Compare this to an input match time.
def check_time(match_time: str) -> bool:
    # Get the minute and hour of current & game times
    current_hour = int(datetime.datetime.now().strftime("%H"))
    current_minute = int(datetime.datetime.now().strftime("%M"))
    match_hour = int(match_time[:match_time.find(":")])
    match_minute = int(match_time[match_time.find(":") + 1:])

    # If the current time is later than the given time, return False
    if current_hour > match_hour:
        return False
    elif current_hour == match_hour:
        if current_minute > match_minute:
            return False
    return True

update_tables()
