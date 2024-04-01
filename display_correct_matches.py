from db_connect_matches import ConnectDbMatch

db_match = ConnectDbMatch()
print("**** Display Settled Games ****")

all_matches = db_match.get_all_matches()
for match in all_matches:
    if match.is_settled:
        print(match.team1 + " vs " + match.team2)

