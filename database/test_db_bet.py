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

print(db.join_bet_with_upcoming_matches("james"))
