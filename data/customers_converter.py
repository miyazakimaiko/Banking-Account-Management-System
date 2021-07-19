import os
import csv
from customer.customers import Customers
from customer.customer import Customer

class CustomersConverter():

    def parse_csv(self):
        customers = Customers()

        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        customers_csv = os.path.join(THIS_FOLDER, 'customers.csv')

        with open(customers_csv, newline='\n') as csv_file:

            for row in csv_file.read().splitlines():
                values = row.split(',')
                fname, lname, ppsn = None, None, None

                for index, value in enumerate(values):
                    if index == 0:
                        fname = value

                    elif index == 1:
                        lname = value

                    elif index == 2:
                        ppsn = value

                customer = Customer(fname, lname, ppsn)
                customers.add(customer)

            csv_file.close()

        return customers


    def format_csv(self, customers):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        customers_csv = os.path.join(THIS_FOLDER, 'customers.csv')

        if os.path.isfile(customers_csv):
            os.remove(customers_csv)

        else:    ## Show an error ##
            print("Error: %s file not found" % customers_csv)

        with open(customers_csv, 'w+', newline='\n') as csv_file:
            writer = csv.writer(csv_file)
            
            for customer in customers.customer_list:

                data = []
                data.append(customer.first_name)
                data.append(customer.last_name)
                data.append(customer.ppsn)
                writer.writerow(data)