from db_bet import ConnectDbBet

db = ConnectDbBet()

# Example of adding bet to db
new_bet = db.add_new_bet(
    username='newMan',
    par_id="fakeID343",
    win=0,