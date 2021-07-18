class Account():

    def __init__(self, balance):
        self._balance = balance
        self._interest_rate = 0.02
        if self._balance > 10000:
            self._interest_rate = 0.05

    @property
    def balance(self):
        return self._balance

    @property
    def iterest_rate(self):
        return self._interest_rate

    def lodge(self, amount):
        self._balance = self._balance + amount


class Current(Account):
    def __init__(self, balance, overdraft):
        super().__init__(balance)
        self._overdraft = overdraft

    @property
    def overdraft(self):
        return self._overdraft

    def withdraw(self, amount):
        if amount < self._balance or self._overdraft is True:
            self._balance = self._balance - amount
            return True
        return False

    def __repr__(self):
        return f"type: current, balance: {self.balance}, interest_rate: {self._interest_rate}, overdtaft: {self.overdraft}"


class Deposit(Account):
    def __repr__(self):
        return f"type: deposit, balance: {self.balance}, interest_rate: {self._interest_rate}"