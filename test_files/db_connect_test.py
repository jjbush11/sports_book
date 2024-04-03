from db_connect_matches import ConnectDbMatch
from db_connect_user import ConnectDbUser
from bet import Bet

db_match = ConnectDbMatch()
db_user = ConnectDbUser()
print("**** Testing user table ****\n")
print("Get existing user info:")
user = db_user.get_row_by_user("jamesBush")
print("Username: " + user.username)
print("Password: " + user.password)
print("Balance: " + str(user.balance))
print("Active Bets: ")
print(user.active_bets)
print("Resolved bets: ")
print(user.resolved_bets)


print("\n**** Testing upcoming matches table ****\n")
match = db_match.get_upcoming_matches_by_id(2)
print("Id: " + str(match.id))
print("Team1: " + match.team1)
print("Team1_odds: " + str(match.team1_odds))
print("Team2: " + match.team2)
print("Team2_odds: " + str(match.team2_odds))

match2 = db_match.get_upcoming_matches_by_id('DucksCanucks')
print(match2)



# print(user.active_bets[0]['return'])

# print(db.add_new_user('sma', 'smaPass'))

# print(db.edit_row('sma', 'balance', 44))
# print(db.get_row_by_user('sma'))


# bet = Bet(id=1, win=0, odds=1000, wager=10)
#
# bet_to_add = bet.bet_to_json()
# # print(bet_to_add)
#
# active_bets_edited = []
# active_bets = user.active_bets
#
# for bet in active_bets:
#     active_bets_edited.append(bet)
#
# active_bets_edited.append(bet_to_add)
#
# print(active_bets_edited)
# db.edit_row('jamesBush', 'active_bets', active_bets_edited)

