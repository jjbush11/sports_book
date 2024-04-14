from db_settled_matches import ConnectDbSettledMatch

db = ConnectDbSettledMatch()

# Example using add_new_settled_match
new_settled = db.add_new_settled_match(
    par_id='VikingPatriots',
    away='Minn Vikings',
    away_score=24,
    home='New England Patriots',
    home_score=21,
    sport="NFL"
)
if new_settled == 1:
    print("Settled match already exists.")
elif new_settled == 2:
    print("Unable to add settled match.")
elif new_settled == 0:
    print("Settled match added successfully.")

# Example using get_all_matches
print(db.get_all_matches())

# Example using get_settled_matches_by_id
print(db.get_settled_matches_by_id('VikingPatriots'))

# Example using does_settled_match_exist
does_exist = db.does_settled_match_exist('VikingPatriots')
if does_exist:
    print("Settled match exists.")
else: print("Settled match does not exist. ")

# Example using edit row, editing the balance
edit = db.edit_settled_match_row('VikingPatriots', 'home_score', 40)
if edit == 1:
    print("Settled match does not exist.")
elif edit == 0:
    print("Edit made.")

# Example removing user
remove = db.remove_settled_match('VikingPatriots')
if remove == 1:
    print("Settled match does not exist.")
elif remove == 0:
    print('Settled match removed.')