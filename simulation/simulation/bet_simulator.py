from numpy import random

from .bet import Bet

class BetSimulator:

    def run(self, starting_balance, bankroll):
        path = random.random(self.n)
        res = []
        balance = starting_balance
        for i in path:
            bet_obj_result = Bet(self.odds, self.edge).result(i)
            bet_pnl = bankroll.calculate(self.odds, bet_obj_result, balance) 
            balance += bet_pnl
            res.append([bet_obj_result, balance])
        return res

    def __init__(self, number_of_bets, avg_odds, edge):
        self.n = number_of_bets
        self.odds = avg_odds
        self.edge = edge
        return


