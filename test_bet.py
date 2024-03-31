from bet import Bet

bet = Bet(id=1, win=0, odds=1000, wager=10)

print(bet.bet_to_json())