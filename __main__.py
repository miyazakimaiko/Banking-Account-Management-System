from data.customers_converter import CustomersConverter
from data.accounts_converter import AccountsConverter
from menu.main_menu import MainMenu

customers = CustomersConverter().parse_csv()
AccountsConverter().parse_csv(customers)

MainMenu().main(customers)