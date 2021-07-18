from .utils import Utils
from customer.customer import Customer

class CreateCustomerMenu():

    def main(self, customers, ppsn):
        Utils().clear_screen()
        print("PPS number entered does not exist in the record. Will create new customer.")
        print()

        first_name = self.get_name_via_input("Please enter first name: ")
        last_name = self.get_name_via_input("Please enter last name: ")
        customer = Customer(first_name, last_name, ppsn)
        customers.add(customer)


    def get_name_via_input(self, message):
        name = input(message)

        if not name.isalnum():
            print('🚫 Wrong format. Only numbers and alphabet are accepted.')
            name = self.get_name_via_input(message)

        return name

    