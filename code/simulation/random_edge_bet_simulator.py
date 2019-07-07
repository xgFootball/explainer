from numpy import random

from bet import Bet

class RandomEdgeBetSimulator:

    def run(self, starting_balance, bankroll):
        path = random.random(self.n)
        res = []
        balance = starting_balance
        for p, e in zip(path, self.edge):
            bet_obj_result = Bet(self.odds, e).result(p)
            bet_pnl = bankroll.calculate(self.odds, bet_obj_result, balance) 
            balance += bet_pnl
            res.append([bet_obj_result, balance])
        return res

    def __init__(self, number_of_bets, avg_odds, edge_mean, edge_stdev):
        self.n = number_of_bets
        self.odds = avg_odds
        self.edge = random.normal(edge_mean, edge_stdev, number_of_bets)
        return

