
class Bet:

    """ Market is saying event will happen with 1/odds
    If your edge - in % terms - is x then event will 
    actually happen with (1/odds)+x
    """
    def result(self, r):
        odds_percent = 1/self.odds
        odds_with_edge = odds_percent + self.edge
        if r < odds_with_edge: return 1
        return -1

    def __init__(self, odds, edge):
        self.odds = odds
        self.edge = edge
        return
