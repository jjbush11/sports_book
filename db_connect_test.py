from db_connect import ConnectDb
from bet import Bet

db = ConnectDb()

user = db.get_row_by_user('jamesBush')

# print(user.username)
# print(user.password)
# print(user.balance)
# print(user.active_bets)
# print(user.resolved_bets)
# print("")
#
# print(user.active_bets[0]['return'])

# print(db.add_new_user('sma', 'smaPass'))

# print(db.edit_row('sma', 'balance', 44))
# print(db.get_row_by_user('sma'))


bet = Bet(id=1, win=0, odds=1000, wager=10)

bet_to_add = bet.bet_to_json()
# print(bet_to_add)

active_bets_edited = []
active_bets = user.active_bets

for bet in active_bets:
    active_bets_edited.append(bet)

active_bets_edited.append(bet_to_add)

print(active_bets_edited)
db.edit_row('jamesBush', 'active_bets', active_bets_edited)

