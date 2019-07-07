
#Bet Simulator#

Run multiple simulations on multiple series of bets. This can be used to infer the probability of certain outcomes or the likely value of certain parameters (i.e. edge). Simple analytics on those results are also offered (i.e. average win streak, average final balance, etc.), as well as statistical tests to compare one result to another (t-statistic and KS).

This package is built to be relatively interchangeable so elements can be substituted and new custom simulations created. Most importantly, new bankroll strategies can be defined and inserted into a simulation without having to alter any other part of the simulation. 

The 3 client scripts demonstrate this. The first script is a simple simulation given constant edge, average odds, and starting balance. The second script substitues the simulator model for one with a random edge with normal distribution. And the final script creates two models with the same bankroll strategies, different simulator models (one is a null hypothesis simulation of just paying the vig), and compares the two results for statistical significane (i.e. is our first model statistically significant against the null of paying the vig).

The call signature for the BankRollStrategy interface is:

    `def calculate(self, odds, bet_result, balance):
         return pnl_of_bet 
    `

The call signature for the BetSimulator interface is:
    
     `def run(self, starting_balance, bankroll):
          return list_containing([bet_results, bankroll_path])
     `
 
 
  
