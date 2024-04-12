from db_upcoming_matches import ConnectDbUpcomingMatch

db = ConnectDbUpcomingMatch()

# Example using add_new_upcoming_match
new_upcoming = db.add_new_upcoming_match(
    id='VikingPatriots',
    home='Minn Vikings',
    home_odds=200,
    away='New England Patriots',
    away_odds=-100,
    date="2024-12-12",
    time="20:00:00"
)
if new_upcoming == 1:
    print("upcoming match already exists.")
elif new_upcoming == 2:
    print("Unable to add upcoming match.")
elif new_upcoming == 0:
    print("upcoming match added successfully.")

# Example using get_all_matches
print(db.get_all_matches())

# Example using get_upcoming_matches_by_id
print(db.get_upcoming_matches_by_id('VikingPatriots'))

# Example using does_upcoming_match_exist
does_exist = db.does_upcoming_match_exist('VikingPatriots')
if does_exist:
    print("upcoming match exists.")
else: print("upcoming match does not exist. ")

# Example using edit row, editing the balance
edit = db.edit_upcoming_match_row('VikingPatriots', 'home_odds', -130)
if edit == 1:
    print("upcoming match does not exist.")
elif edit == 0:
    print("Edit made.")

# Example removing user
remove = db.remove_upcoming_match('VikingPatriots')
if remove == 1:
    print("upcoming match does not exist.")
elif remove == 0:
    print('upcoming match removed.')