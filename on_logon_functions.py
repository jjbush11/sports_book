# Logon behavior functions file
from database.db_connect_user import ConnectDbUser
from database.matches_to_database import main


# Check the user's balance. Set it to $5 if it is less than $5.
def check_balance(username: str) -> None:
    user = ConnectDbUser()
    user_balance = user.get_row_by_user(username).balance

    if user_balance < 5:
        user.edit_row(username, "balance", 5)


# On startup: update the current matchups
def update_tables() -> None:
    main()


def check_if_settled() -> None:
    # For all user bets that are not paid out:
    # Check if match ID is in settled matches:
    # If it's there, and mark the bet as settled and pay out if they won.
