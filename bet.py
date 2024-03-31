import uuid
class Bet:

    id = -1
    win = 0
    odds = 0
    wager = -1
    return_val = -1

    def __init__(self, win, odds, wager):
        self.id = uuid.uuid4()
        self.win = win
        self.odds = odds
        self.wager = wager
        self.return_val = self.get_return_val()

    def get_return_val(self) -> float:
        if self.odds > 0:
            self.return_val = self.wager * (self.odds / 100)
        else:
            self.return_val = self.wager / (-self.odds / 100)

        return self.return_val

    def set_win(self, is_win):
        self.win = is_win

    def bet_to_dict(self):
        # Define string in formt of json

        bet_dict = {
            'id': self.id,
            'win': self.win,
            'odds': self.odds,
            'wager': self.wager,
            'return': self.return_val
        }

        return bet_dict


