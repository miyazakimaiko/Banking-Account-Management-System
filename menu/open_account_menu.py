from .utils import Utils
from account.account import Current, Deposit

class OpenAccountMenu():

    def main(self, customers):
        Utils().clear_screen()
        print()
        print('Selected: 1. Open new account')
        print()

        ppsn = self.get_ppsn_via_input()
        customer = customers.get_customer_by_ppsn(ppsn)

        if not customer:
            from .create_customer_menu import CreateCustomerMenu
            CreateCustomerMenu().main(customers, ppsn)
            customer = customers.get_customer_by_ppsn(ppsn)

        Utils().clear_screen()

        print("Customer: ", customer.first_name, customer.last_name)
        print()
        self.create_account(customer)


    def get_ppsn_via_input(self):
        ppsn = input('Please enter PPS number: ')

        if not ppsn.isalnum():
            print('🚫 Wrong format. Only numbers and alphabet are accepted.')
            ppsn = self.get_ppsn_via_input()

        return ppsn


    def create_account(self, customer):
        account_type = self.get_account_type_via_input()
        Utils().clear_screen()
        print()

        if account_type == 1:
            balance = self.get_initial_balance_via_input(account_type)
            overdraft = self.get_overdraft_bool_via_input()
            account = Current(balance, overdraft)
            customer.add_account(account)

        elif account_type == 2:
            balance = self.get_initial_balance_via_input(account_type)
            account = Deposit(balance)
            customer.add_account(account)

        Utils().clear_screen()
        print()
        print("✅ New account is opened for ", customer.first_name, customer.last_name)
        print()
        print(" ".ljust(30), "Accounts")
        print("-"*75)
        for account in customer.accounts.items():
            print(account)
        print()

    def get_account_type_via_input(self):
        type = input('Enter a number for the account type you wish to open (1: CURRENT, 2: DEPOSIT): ')

        try:
            type = int(type)
        except:
            print('🚫 Wrong format. Please enter a digit.')
            type = self.get_account_type_via_input()

        if type not in [1, 2]:
            print('🚫 Selection out of range. Please enter a digit 1 or 2.')
            type = self.get_account_type_via_input()

        return type


    def get_overdraft_bool_via_input(self):
        choice = input('Register for the overdraft facility (Y/N): ')

        if choice not in ['Y', 'y', 'N', 'n']:
            print('🚫 Wrong format. Please enter Y or N.')
            choice = self.get_overdraft_bool_via_input()

        elif choice in ['Y', 'y']:
            choice = True

        elif choice in ['N', 'n']:
            choice = False

        return choice


    def get_initial_balance_via_input(self, account_type):
        amount = input('Enter initial balance to lodge: ')

        try:
            amount = float(amount)
        except:
            print('🚫 Wrong format. Please enter a number.')
            amount = self.get_initial_balance_via_input(account_type)

        # when account_type is current..
        if account_type == 1 and amount < 25:
            print('🚫 Minimum amount is ¢25.')
            amount = self.get_initial_balance_via_input(account_type)

        # when account_type is deposit..
        elif account_type == 2 and amount < 50:
            print('🚫 Minimum amount is ¢50.')
            amount = self.get_initial_balance_via_input(account_type)

        return amount