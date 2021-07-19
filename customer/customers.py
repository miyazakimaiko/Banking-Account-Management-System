class Customers():
    def __init__(self):
        self._customer_list = []

    @property
    def customer_list(self):
        return self._customer_list

    def add(self, customer):
        self._customer_list.append(customer)

    def get_customer_by_ppsn(self, ppsn):
        for customer in self.customer_list:
            if customer.ppsn == ppsn:
                return customer
        return

    def __repr__(self):
        result = ""
        for customer_obj in self._customer_list:
            customer_str = ""
            customer_str += "First name: "
            customer_str += customer_obj.first_name
            customer_str += ", "
            customer_str += "Last name: "
            customer_str += customer_obj.last_name
            customer_str += ", "
            customer_str += "PPSN: "
            customer_str += customer_obj.ppsn
            customer_str += "\n"
            result += customer_str
        return result