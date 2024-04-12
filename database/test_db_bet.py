from db_bet import ConnectDbBet

db = ConnectDbBet()

# Example of adding bet to db
new_bet = db.add_new_bet(
    username='newMan',
    par_id="fakeID33",
    win=0,
    odds=300,
    wager=10,
    settled=0
)
if new_bet == 1:
    print("bet match already exists.")
elif new_bet == 2:
    print("Unable to add bet match.")
elif new_bet == 0:
    print("bet match added successfully.")

# Get all bets
# Get
print(db.get_all_active_bets_by_user('james'))