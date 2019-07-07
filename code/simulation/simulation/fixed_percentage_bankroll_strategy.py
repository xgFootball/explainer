

class FixedPercentageBankrollStrategy:

    @staticmethod
    def __logic(percentage, current_balance):
        return percentage * current_balance

    def calculate(self, odds, res, balance):
        if balance < 1:
            return 0
        bet_size = FixedPercentageBankrollStrategy.__logic(self.percentage, balance)
        pnl = res * (bet_size * odds)
        return round(pnl,2)

    def __init__(self, percentage_of_balance):
        self.percentage = percentage_of_balance
        return
