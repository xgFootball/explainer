from simulation_results import SimulationResults

class SimulationRunner:

    def run(self):
        bet_results = []
        bankroll_paths = []
        for i in range(self.n):
            results = self.simulator.run(self.starting_balance, self.bankroll)
            bet_result, bankroll_path = list(zip(*results))
            bet_results.append(bet_result)
            bankroll_paths.append(bankroll_path)
        return SimulationResults(bet_results, bankroll_paths)

    def __init__(self, number_of_sims, starting_balance, simulator_obj, bankroll_strategy_obj):
        self.n = number_of_sims
        self.starting_balance = starting_balance
        self.simulator = simulator_obj
        self.bankroll = bankroll_strategy_obj
        return

