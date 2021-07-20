class Account():

    def __init__(self, balance):
        self._balance = balance
        self._interest_rate = 0.02
        self.reflect_interest_rate()

    @property
    def balance(self):
        return self._balance

    @property
    def iterest_rate(self):
        return self._interest_rate

    def is_transferrable(self, amount):
        if amount <= self._balance:
            return True
        return False

    def send(self, amount):
        self._balance = round((self._balance - amount), 2)
        self.reflect_interest_rate()

    def receive(self, amount):
        self._balance = round((self._balance + amount), 2)
        self.reflect_interest_rate()

    def lodge(self, amount):
        self._balance = round((self._balance + amount), 2)
        self.reflect_interest_rate()

    def reflect_interest_rate(self):
        if self._balance > 10000:
            self._interest_rate = 0.05
        else:
            self._interest_rate = 0.02




class Current(Account):
    def __init__(self, balance, overdraft):
        super().__init__(balance)
        self._overdraft = overdraft

    @property
    def overdraft(self):
        return self._overdraft

    def is_transferrable(self, amount):
        if amount <= self._balance or self._overdraft is True:
            return True
        return False

    def is_withdrawable(self, amount):
        if amount <= self._balance or self._overdraft is True:
            return True
        return False

    def withdraw(self, amount):
        if amount <= self._balance or self._overdraft is True:
            self._balance = round((self._balance - amount), 2)
            self.reflect_interest_rate()
            return True
        return False

    def __repr__(self):
        return f"type: current, balance: {self.balance}, interest_rate: {self._interest_rate}, overdtaft: {self.overdraft}"


class Deposit(Account):
    def __repr__(self):
        return f"type: deposit, balance: {self.balance}, interest_rate: {self._interest_rate}"