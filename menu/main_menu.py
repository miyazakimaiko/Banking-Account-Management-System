from .utils import Utils
from data.accounts_converter import AccountsConverter
from data.customers_converter import CustomersConverter

class MainMenu():

    def main(self, customers):
        Utils().clear_screen()
        self.display_options()

        selection = self.get_selection_via_input()

        if selection == 1:
            from .open_account_menu import OpenAccountMenu
            OpenAccountMenu().main(customers)

        elif selection == 2:
            from .withdrawal_menu import WithdrawalMenu
            WithdrawalMenu().main(customers)

        elif selection == 3:
            from .lodgement_menu import LodgementMenu
            LodgementMenu().main(customers)

        elif selection == 4:
            from .transfer_menu import TransferMenu
            TransferMenu().main(customers)

        elif selection == 5:
            from .view_accounts_menu import ViewAccountsMenu
            ViewAccountsMenu().main(customers)

        elif selection == 6:
            Utils().clear_screen()
            self.display_onscreen_help()

        elif selection == 7:
            Utils().clear_screen()
            AccountsConverter().format_csv(customers)
            CustomersConverter().format_csv(customers)
            print('Changes have saved successfully.')
            print()
            return

        print()
        input('Press Enter to go back to Menu...')
        self.main(customers)


    def display_options(self):
        print()
        print("Main Menu")
        print()
        print("______Options_____")
        print()
        print("1. Open new account")
        print("2. Withdrawal")
        print("3. Lodgement")
        print("4. Transfer")
        print("5. View accounts")
        print("6. Onscreen help")
        print("7. Close")
        print()


    def get_selection_via_input(self):
        selection = input('Please enter a number (1 - 7): ')

        try:
            selection = int(selection)
        except:
            print('🚫 Wrong format. Please enter a digit.')
            selection = self.get_selection_via_input()

        if selection > 7 or selection < 1:
            print('🚫 Selection out of range. Please enter a digit between 1 and 7.')
            selection = self.get_selection_via_input()

        return selection


    def display_onscreen_help(self):
        print()
        print("Onscreen help")
        print()
        print("Selection 1: Open New Account")
        print("This menu allows you to open an account for existing customer, or navigate through to")
        print("register customer first if they do not exist on the system.")
        print()
        print("Selection 2: Withdrawal")
        print("This menu allows you to withdraw required amount from a Current account.")
        print()
        print("Selection 3: Lodgement")
        print("This menu allows you to lodge required amount to either Current or Deposit account.")
        print()
        print("Selection 4: Transfer")
        print("This menu allows you to transfer required amount from one account to another.")
        print()
        print("Selection 5: View Accounts")
        print("This menu allows you to view all accounts, or accounts of a specified customer.")
        print()
        print("Selection 7: Close")
        print("This selection allows you to save all the changes made on the session and close the ")
        print("system safely.")
        print()
        print("If you need any assistance, please call 0834837641.")