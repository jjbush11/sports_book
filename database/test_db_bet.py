from db_bet import ConnectDbBet

db = ConnectDbBet()

# Example of adding bet to db
# new_bet = db.add_new_bet(
#     username='newMan',
#     par_id="fakeID343",
#     win=0,
#     odds=300,
#     wager=10,
#     settled=0
# )
# if new_bet == 1:
#     print("bet already exists.")
# elif new_bet == 2:
#     print("Unable to add bet.")
# elif new_bet == 0:
#     print("bet added successfully.")
#
#
# # Get all bets
# all_bets = db.get_all_bets()
# if len(all_bets) > 0:
#     print("Get all bets successful.")
# else:
#     print("FAILED: Get all bets")
#
# # Get bet by id
# by_id = db.get_bet_by_id("fakeID33")
# if by_id == None:
#     print("FAILED: get bet by id.")
# else:
#     print("PASSED: get row by id")
#
# # Get all active bets by user
# print(db.get_all_active_bets_by_user('james'))
#
# # Get all settled bets by user
# print(db.get_all_settled_bets_by_user('newMan'))

new_bet = db.add_new_bet(
    username='newMan',
    par_id="fakeID343",
    win=0,
    odds=300,
    wager=10,
    settled=0
)

#Add test matches for settled bets
test_bet1 = db.add_new_bet(
    username='fart',
    par_id="BostonCharlotteApr 12",
    win=0,
    odds=300,
    wager=10,
    settled=1
)

test_bet2 =  db.add_new_bet(
    username='fart',
    par_id="Houston AstrosTexas RangersApr 12",
    win=1,
    odds=200,
    wager=20,
    settled=1
)

#Add test matches for active bets
test_bet3 = db.add_new_bet(
    username='fart',
    par_id= "Seattle KrakenSt. Louis BluesApr 14",
    win=1,
    odds=500,
    wager=30,
    settled=0
)

test_bet4 =  db.add_new_bet(
    username='fart',
    par_id="Chicago BullsNew York KnicksApr 14",
    win=1,
    odds=200,
    wager=20,
    settled=0
)

test_bet5 =  db.add_new_bet(
    username='fart',
    par_id="Cincinnati RedsChicago White SoxApr 14",
    win=0,
    odds=300,
    wager=10,
    settled=0
)


if new_bet == 1:
    print("bet already exists.")
elif new_bet == 2:
    print("Unable to add bet.")
elif new_bet == 0:
    print("bet added successfully.")

print(db.join_bet_with_upcoming_matches("james"))
