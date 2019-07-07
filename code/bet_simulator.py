from numpy import random

def simulate_path(number_of_bets, avg_odds, edge):

    avg_odds_percent = 1 / avg_odds
    ##market is saying this event will happen 1/avg_odds
    ##if your edge (in % terms) is x then the event
    ##actually happens (1/avg_odds) - x
    avg_odds_with_edge = avg_odds_percent - edge

    path = random.random(number_of_bets)
    result = []
    for i in path:
        if i > avg_odds_with_edge:
            result.append(1)
        else:
            result.append(0)
    return result

def simulation_runner(number_of_sims, bets_per_sim, avg_odds, edge):
    for i in range(number_of_sims):
        result = simulate_path(bets_per_sim, avg_odds, edge)


if __name__ == "__main__":

    print(simulate_bet(2.0, 0.05))
    print(simulate_bet(2.0, 0.25))



