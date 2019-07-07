from simulation_runner import SimulationRunner
from bet_simulator import BetSimulator
from fixed_percentage_bankroll_strategy import FixedPercentageBankrollStrategy 

if __name__ == "__main__":

    bankroll_strategy = FixedPercentageBankrollStrategy(
        percentage_of_balance = 0.05
    )

    bet_sim = BetSimulator(
        number_of_bets = 100, 
        avg_odds = 2.00, 
        edge = -0.1
    )
    
    sim = SimulationRunner(
        number_of_sims = 10, 
        starting_balance = 10000,
        simulator_obj = bet_sim, 
        bankroll_strategy_obj = bankroll_strategy
    )

    res = sim.run()
    print(res.summary())
