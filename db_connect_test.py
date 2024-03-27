
from db_connect import ConnectDb

db = ConnectDb()

user = db.get_row_by_user('dsds')
print(type(user))
print(user!=None)

# print(user.username)
# print(user.password)
# print(user.balance)
# print(user.active_bets)
# print(user.resolved_bets)
# print("")
#
# print(user.active_bets[0]['return'])

# print(db.add_new_user('sma', 'smaPass'))


