from db_connect_matches import ConnectDbMatch

db_match = ConnectDbMatch()
print("**** Display Settled Games ****")

# db_match.edit_upcoming_match_row('JacketsAvalanche', 'time', '19:30:00')
# db_match.edit_upcoming_match_row('DucksCanucks', 'time', '20:00:00')

all_matches = db_match.get_all_matches()
for match in all_matches:
    db_match.check_and_set_if_match_settled(match.id)
    # print(match.id)
    # if match.is_settled:
    #     print("Settled Game: " + match.team1 + " vs " + match.team2)
    #
    # elif not match.is_settled:
    #     print("Not settled Game: " + match.team1 + " vs " + match.team2)
