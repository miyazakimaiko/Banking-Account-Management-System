class Customers():
    def __init__(self):
        self._customers_list = []

    @property
    def customer_list(self):
        return self._customers_list

    def add(self, customer):
        self._customers_list.append(customer)

    def get_customer_by_ppsn(self, ppsn):
        for customer in self.customer_list:
            if customer.ppsn == ppsn:
                return customer
        return

    def __repr__(self):
        for customer in self.customer_list:
            print(customer)
        return