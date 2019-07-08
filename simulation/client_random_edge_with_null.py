from simulation.simulation_runner import SimulationRunner
from simulation.random_edge_bet_simulator import RandomEdgeBetSimulator
from simulation.fixed_percentage_bankroll_strategy import FixedPercentageBankrollStrategy 

if __name__ == "__main__":

    bankroll_strategy = FixedPercentageBankrollStrategy(
        percentage_of_balance = 0.025
    )

    number_of_bets = 1000
    odds = 2.00
    number_of_sims = 10
    starting_balance = 10000

    bet_sim = RandomEdgeBetSimulator(
        number_of_bets = number_of_bets,
        avg_odds = odds, 
        edge_mean = 0.025,
        edge_stdev = 0.1
    )
    
    sim = SimulationRunner(
        number_of_sims = number_of_sims,
        starting_balance = starting_balance,
        simulator_obj = bet_sim, 
        bankroll_strategy_obj = bankroll_strategy
    )

    bet_sim_null = RandomEdgeBetSimulator(
        number_of_bets = number_of_bets,
        avg_odds = odds,
        edge_mean = -0.025,
        edge_stdev = 0.0,
    )

    sim_null = SimulationRunner(
        number_of_sims = number_of_sims, 
        starting_balance = starting_balance,
        simulator_obj = bet_sim_null, 
        bankroll_strategy_obj = bankroll_strategy
    )

    h1 = sim.run()
    print(h1.summary())
    h0 = sim_null.run()
    print(h0.summary())
    print(h1.significance_test_final_balance(h0.bankroll))
    print(h1.kstest_final_balance(h0.bankroll))


