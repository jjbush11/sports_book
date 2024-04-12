from db_connect_user import ConnectDbUser

db = ConnectDbUser()

# Example using add_new_user
add_new_user = db.add_new_user(
    username="exampleUser",
    password="example"
)
if add_new_user == 1:
    print("User already exists.")
elif add_new_user == 2:
    print("Unable to add user.")
elif add_new_user == 0:
    print("User added successfully.")

# Example using get_row_by_user
print(db.get_row_by_user('exampleUser'))

# Example using edit row, editing the balance
edit = db.edit_row('exampleUser', 'balance', 40)
if edit == 1:
    print("User does not exist.")
elif edit == 0:
    print("Edit made.")

# Example removing user
remove = db.remove_user('exampleUser')
if remove == 1:
    print("User does not exist.")
elif remove == 0:
    print('User removed.')
