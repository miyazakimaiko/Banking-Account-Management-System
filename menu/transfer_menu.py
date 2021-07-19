from .utils import Utils

class TransferMenu():

    def main(self, customers):
        Utils().clear_screen()
        print('Selected: 4. Transfer')
        print()
        print('SENDER Details')
        print()
        sender = self.get_account(customers)
        receiver = None

        if sender:
            print()
            print('RECEIVER Details')
            print()
            receiver = self.get_account(customers)

        if sender and receiver:
            amount = self.get_transferrable_amount_via_input(sender)
            sender.send(amount)
            receiver.receive(amount)
            
            Utils().clear_screen()
            print()
            print("Transfer successful.")
            print()
            print('Amount transferred: ', amount)
            print('Sender', sender)
            print('Receiver', receiver)


    def get_account(self, customers):
        ppsn = self.get_ppsn_via_input()
        customer = customers.get_customer_by_ppsn(ppsn)

        if not customer:
            print("🚫 Customer does not exist.")
            print()
            
        else:
            print()
            print("____Customer Detail____")
            print("First name: ", customer.first_name)
            print("Last name: ", customer.last_name)
            print("PPSN: ", customer.ppsn)
            print()
            account_number = input('Please enter account number: ')

            if account_number in customer.accounts:
                return customer.accounts[account_number]
            else:
                print('🚫 Account does not exist.')
                return


    def get_ppsn_via_input(self):
        ppsn = input('Please enter PPS number: ')

        if not ppsn.isalnum():
            print('🚫 Wrong format. Only numbers and alphabet are accepted.')
            ppsn = self.get_ppsn_via_input()

        return ppsn


    def get_transferrable_amount_via_input(self, account):
        amount = input(f"Please enter amount to transfer: ")

        try:
            amount = round(float(amount), 2)
        except:
            print('🚫 Wrong format. Please enter a digit.')
            amount = self.get_transferrable_amount_via_input(account)

        if amount < 5 or amount > 250000:
            print('🚫 The minimum of ¢5 to the maximum of ¢250,000 can be transferred at once.')

        elif not account.is_transferrable(amount):
            print('🚫 The amount entered is not transferrable from the sender. Please enter different amount.')
            amount = self.get_transferrable_amount_via_input(account)

        return amount          