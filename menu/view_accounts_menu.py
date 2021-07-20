from account.account import Current, Deposit
from .utils import Utils

class ViewAccountsMenu():

    def main(self, customers):
        Utils().clear_screen()
        print('Selected: 5. View accounts')
        self.display_options()

        selection = self.get_selection_via_input()

        if selection == 1:
            self.display_all_accounts(customers)

        elif selection == 2:
            ppsn = self.get_ppsn_via_input()
            customer = self.get_customer_by_ppsn(ppsn, customers)

            if customer:
                self.display_accounts_of_cusomter(customer)
            else:
                print()
                print("🚫 Customer with the PPSN does not exist.")


    def display_options(self):
        print()
        print("______Options_____")
        print()
        print("1. View all accounts")
        print("2. Find accounts by PPS number")
        print()


    def get_selection_via_input(self):
        selection = input('Please enter a number (1 - 2): ')

        try:
            selection = int(selection)
        except:
            print('🚫 Wrong format. Please enter a digit.')
            selection = self.get_selection_via_input()

        if selection not in [1, 2]:
            print('🚫 Selection out of range. Please enter a digit between 1 or 2.')
            selection = self.get_selection_via_input()

        return selection

    
    def display_all_accounts(self, customers):
        Utils().clear_screen()
        print()
        print("All Accounts")
        print()
        print("FirstName".ljust(20)+"LastName".ljust(20)+"AccountNumber".ljust(20)+"Balance".ljust(20)+"InterestRate")
        print("-"*100)
        fname, lname, acc_num, balance, int_rate = (None,)*5

        for customer in customers.customer_list:
            fname = str(customer.first_name).ljust(20)
            lname = str(customer.last_name).ljust(20)

            for number, account in customer.accounts.items():
                acc_num = str(number).ljust(20)
                balance = str(account.balance).ljust(20)
                int_rate = str(account.iterest_rate)

                print(f"{fname}{lname}{acc_num}{balance}{int_rate}")


    def get_ppsn_via_input(self):
        ppsn = input('Please enter PPS number: ')

        if not ppsn.isalnum():
            print('🚫 Wrong format. Only numbers and alphabet are accepted.')
            ppsn = self.get_ppsn_via_input()

        return ppsn


    def get_customer_by_ppsn(self, ppsn, customers):
        for customer in customers.customer_list:
            if customer.ppsn == ppsn:
                return customer
        return


    def display_accounts_of_cusomter(self, customer):
        Utils().clear_screen()
        print()
        print("Customer")
        print()
        print("First Name: ", customer.first_name)
        print("Last Name: ", customer.last_name)
        print("PPSN: ", customer.ppsn)
        print()
        print()
        print("Accounts")
        print()
        print("AccountNumber".ljust(20)+"AccountType".ljust(20)+"Overdraft".ljust(20)+"Balance".ljust(20)+"InterestRate")
        print("-"*92)

        acc_num, acc_type, overdraft, balance, int_rate = (None,)*5

        for number, account in customer.accounts.items():
            acc_num = str(number).ljust(20)
            balance = str(account.balance).ljust(20)
            int_rate = str(account.iterest_rate).ljust(20)

            if isinstance(account, Current):
                acc_type = "Current".ljust(20)
                if account.overdraft:
                    overdraft = "Y".ljust(20)
                elif not account.overdraft:
                    overdraft = "N".ljust(20)

            elif isinstance(account, Deposit):
                acc_type = "Deposit".ljust(20)
                overdraft = "".ljust(20)

            print(f"{acc_num}{acc_type}{overdraft}{balance}{int_rate}")