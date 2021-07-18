from .utils import Utils

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
            LodgementMenu().main()

        elif selection == 4:
            from .transfer_menu import TransferMenu
            TransferMenu().main()

        elif selection == 5:
            Utils().clear_screen()
            print('Exiting...')

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
        print("5. Close")
        print()


    def get_selection_via_input(self):
        selection = input('Please enter a number (1 - 5): ')

        try:
            selection = int(selection)
        except:
            print('🚫 Wrong format. Please enter a digit.')
            selection = self.get_selection_via_input()

        if selection > 5 or selection < 1:
            print('🚫 Selection out of range. Please enter a digit between 1 and 5.')
            selection = self.get_selection_via_input()

        return selection