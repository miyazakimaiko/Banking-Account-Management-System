from account.account import Current, Deposit
import os
import csv

class AccountsConverter():

    def parse_csv(self, customers):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        customers_csv = os.path.join(THIS_FOLDER, 'accounts.csv')

        with open(customers_csv, newline='\n') as csv_file:

            for row in csv_file.read().splitlines():
                values = row.split(',')
                customer, account, ppsn, acc_num, acc_type, balance, overdraft = (None,)*7

                for index, value in enumerate(values):
                    if index == 0:
                        ppsn = value

                    elif index == 1:
                        acc_num = value

                    elif index == 2:
                        acc_type = int(value)

                    elif index == 3:
                        balance = float(value)

                    elif index == 4:
                        overdraft = False
                        if value == 'True':
                            overdraft = True

                if acc_type == 1:
                    account = Current(balance, overdraft)
                    
                elif acc_type == 2:
                    account = Deposit(balance)

                for cust in customers.customer_list:
                    if cust.ppsn == ppsn:
                        customer = cust
                        break

                if customer:
                    customer.add_account(account, number=acc_num)
                else:
                    print("customer not found")

            csv_file.close()


    def format_csv(self, customers):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        accounts_csv = os.path.join(THIS_FOLDER, 'accounts.csv')

        if os.path.isfile(accounts_csv):
            os.remove(accounts_csv)

        else:    ## Show an error ##
            print("Error: %s file not found" % accounts_csv)

        with open(accounts_csv, 'w+', newline='\n') as csv_file:
            writer = csv.writer(csv_file)
            
            for customer in customers.customer_list:

                for key, value in customer.accounts.items():
                    ppsn, acc_num, acc_type, balance, overdraft = (None,)*5

                    ppsn = customer.ppsn
                    acc_num = key
                    if isinstance(value, Current):
                        acc_type = 1
                        overdraft = value.overdraft
                    elif isinstance(value, Deposit):
                        acc_type = 2
                    balance = value.balance

                    data = []
                    data.append(ppsn)
                    data.append(acc_num)
                    data.append(acc_type)
                    data.append(balance)
                    data.append(overdraft)
                    writer.writerow(data)