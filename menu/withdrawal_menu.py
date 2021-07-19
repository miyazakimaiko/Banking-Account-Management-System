from .utils import Utils
from account.account import Current, Deposit

class WithdrawalMenu():

    def main(self, customers):
        Utils().clear_screen()
        print('Selected: 2. Withdrawal')

        ppsn = self.get_ppsn_via_input()
        customer = customers.get_customer_by_ppsn(ppsn)

        if not customer:
            print("🚫 Customer does not exist.")
            print()

        else:
            Utils().clear_screen()
            print("____Customer Detail____")
            print("First name: ", customer.first_name)
            print("Last name: ", customer.last_name)
            print("PPSN: ", customer.ppsn)
            print()
            account_number = input('Please enter account number: ')
            account = self.get_account(account_number, customer)

            if isinstance(account, Current):
                print()
                print("Account type: Current")
                print()
                amount = self.get_withdrawable_amount_via_input(account)
                account.withdraw(amount)

                print()
                print("Withdrawal successful")
                print()
                print("Withdrawn: ¢", amount)
                print("Balance: ¢", account.balance)
                print()
                    

            elif isinstance(account, Deposit):
                print()
                print("Account type: Deposit")
                print()
                print("🚫 Cannot withdraw from Deposit account.")

            else:
                print("🚫 Account does not exist.")


    def get_ppsn_via_input(self):
        ppsn = input('Please enter PPS number: ')

        if not ppsn.isalnum():
            print('🚫 Wrong format. Only numbers and alphabet are accepted.')
            ppsn = self.get_ppsn_via_input()

        return ppsn

    
    def get_account(self, num, customer):
        if num in customer.accounts:
            return customer.accounts[num]
        return


    def get_withdrawable_amount_via_input(self, account):
        amount = input('Please enter amount to withdraw: ')

        try:
            amount = round(float(amount), 2)
            
        except:
            print('🚫 Wrong format. Please enter a digit.')
            amount = self.get_withdrawable_amount_via_input(account)

        if amount < 5 or amount > 20000:
            print('🚫 The minimum of ¢5 to the maximum of ¢20,000 can be withdrawn at once.')

        elif not account.is_withdrawable(amount):
            print('🚫 The amount entered is not withdwawable. Please enter different amount.')
            amount = self.get_withdrawable_amount_via_input(account)

        return amount