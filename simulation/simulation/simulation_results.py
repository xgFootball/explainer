from numpy import percentile
from scipy import stats
from itertools import groupby

def _sequence_finder(val, array):
    max_streak = 0
    count = 0
    for i, r in enumerate(array):
        if i == 0 and r == val:
            count=1
        else:
            if r == val:
                count+=1
            else:
                count=0
        if count > max_streak:
            max_streak = count
    return max_streak

class SimulationResults:

    def summary(self):
        print("Average final balance: " + str(self.average_final_balance()))
        print("Average Win %: " + str(self.win_percentage()))
        print("Average max balance: " + str(self.average_max_balance()))
        print("Average min balance: " + str(self.average_min_balance()))
        print("Average longest win streak: " + str(self.avg_longest_win_streak()))
        print("Average longest lose streak: " + str(self.avg_longest_lose_streak()))
        print("95th bankroll percentile: " + str(self.percentile95()))
        print("5th bankroll percentile: " + str(self.percentile5()))
        print("Median bankroll: " + str(self.percentile50()))

    def win_percentage(self):
        res = []
        for res_array in self.results:
            res.append(len(list(filter(lambda r: r==1, res_array)))/len(res_array))
        return round(sum(res)/len(res), 2)

    def avg_longest_win_streak(self):
        res = []
        for res_array in self.results:
            res.append(_sequence_finder(1, res_array))
        return round(sum(res)/len(res), 1)
            
    def avg_longest_lose_streak(self):
        res = []
        for res_array in self.results:
            res.append(_sequence_finder(-1, res_array))
        return round(sum(res)/len(res), 1)

    def percentile95(self):
        return percentile(self.bankroll, 90)

    def percentile5(self):
        return percentile(self.bankroll, 5)

    def percentile50(self):
        return percentile(self.bankroll, 50)

    def average_final_balance(self):
        final = [i[-1] for i in self.bankroll]
        return round(sum(final)/len(final),2)

    def average_max_balance(self):
        max_balances = []
        for i in self.bankroll:
            max_value = 0
            for b in i:
                if b > max_value: max_value=b
            max_balances.append(max_value)
        return round(sum(max_balances)/len(max_balances), 2)

    def average_min_balance(self):
        min_balances = []
        for i in self.bankroll:
            min_value = i[0]
            for b in i:
                if b < min_value: min_value=b
            min_balances.append(min_value)
        return round(sum(min_balances)/len(min_balances), 2)

    def kstest_final_balance(self, null_hypothesis_bankroll):
        final = [i[-1] for i in self.bankroll]
        final_null = [i[-1] for i in null_hypothesis_bankroll]
        ksstat = stats.ks_2samp(final, final_null)
        return "ks-stat: " + str(ksstat[0]) + ", p-value: " + str(ksstat[1])

    def significance_test_final_balance(self, null_hypothesis_bankroll):
        final = [i[-1] for i in self.bankroll]
        final_null = [i[-1] for i in null_hypothesis_bankroll]
        tstat = stats.ttest_ind(final, final_null)
        return "t-stat: " + str(tstat.statistic) + ", p-value: " + str(tstat.pvalue)

    def __init__(self, results_path, bankroll_path):
        self.results = results_path
        self.bankroll = bankroll_path

