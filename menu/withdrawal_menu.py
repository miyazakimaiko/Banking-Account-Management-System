from .utils import Utils

class WithdrawalMenu():

    def main(self, customers):
        Utils().clear_screen()
        print('Selected: 2. Withdrawal')

        ppsn = self.get_ppsn_via_input()
        customer = self.get_customer(ppsn, customers)

        if not customer:
            print("🚫 Customer does not exist.")
            print()
            return

        else:
            print("customer exist.")


    def get_ppsn_via_input(self):
        ppsn = input('Please enter PPS number: ')

        if not ppsn.isalnum():
            print('🚫 Wrong format. Only numbers and alphabet are accepted.')
            ppsn = self.get_ppsn_via_input()

        return ppsn


    def get_customer(self, ppsn, customers):
        return customers.get_customer_by_ppsn(ppsn)