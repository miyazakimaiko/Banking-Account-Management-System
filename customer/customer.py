import random
import string

class Customer():

    def __init__(self, fname, lname, ppsn):
        self._first_name = fname
        self._last_name = lname
        self._ppsn = ppsn
        self._accounts = {}

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ppsn(self):
        return self._ppsn

    @property
    def accounts(self):
        return self._accounts


    def add_account(self, account, number=None):
        if number is None:
            number = self.get_unique_number()
        self._accounts[number] = account


    def get_unique_number(self):
        num = self.create_number()
        unique = False
        while not unique:
            if not self.get_account_by_number(num):
                unique = True
            else:
                num = self.create_number()
        return num


    def create_number(self):
        return ''.join(random.choices(string.digits, k=5))


    def get_account_by_number(self, num):
        for key in self.accounts:
            print(key)
            if key == num:
                return self.accounts[key]
        return False


    def __repr__(self):
        first_name = str(self.first_name).ljust(20)
        last_name = str(self.last_name).ljust(20)
        ppsn = str(self.ppsn).ljust(20)
        accounts = [key for key in self.accounts]
        return f"{first_name}{last_name}{ppsn}{accounts}"