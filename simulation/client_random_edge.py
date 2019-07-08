from simulation.simulation_runner import SimulationRunner
from simulation.random_edge_bet_simulator import RandomEdgeBetSimulator
from simulation.fixed_percentage_bankroll_strategy import FixedPercentageBankrollStrategy 

if __name__ == "__main__":

    bankroll_strategy = FixedPercentageBankrollStrategy(
        percentage_of_balance = 0.01
    )

    bet_sim = RandomEdgeBetSimulator(
        number_of_bets = 1000, 
        avg_odds = 2.00, 
        edge_mean = 0.05,
        edge_stdev = 0.1
    )
    
    sim = SimulationRunner(
        number_of_sims = 100, 
        starting_balance = 10000,
        simulator_obj = bet_sim, 
        bankroll_strategy_obj = bankroll_strategy
    )

    res = sim.run()
    res.summary()


