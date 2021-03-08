class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    def __repr__(self):
        result = ""
        for c in self.customers:
            result += f"{c}\n"
        for dvd in self.dvds:
            result += f"{dvd}\n"
        return result

    @staticmethod
    def can_add_customer(capacity_customer, list_customer):
        return capacity_customer > len(list_customer)

    @staticmethod
    def can_add_dvd(dvd_capacity, dvds_list):
        return dvd_capacity > len(dvds_list)

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    @staticmethod
    def get_dvd_by_id(dvd_list, dvd_id):
        return [dvd for dvd in dvd_list if dvd.id == dvd_id][0]

    @staticmethod
    def get_customer_from_id(customer_list, cust_id):
        return [customer for customer in customer_list if customer.id == cust_id][0]

    def add_customer(self, customer):
        if self.can_add_customer(self.customer_capacity(), self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if self.can_add_dvd(self.dvd_capacity(), self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        dvd = self.get_dvd_by_id(self.dvds, dvd_id)
        customer = self.get_customer_from_id(self.customers, customer_id)
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = self.get_dvd_by_id(self.dvds, dvd_id)
        customer = self.get_customer_from_id(self.customers, customer_id)
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"
        dvd.is_rented = False
        customer.rented_dvds.remove(dvd)
        return f"{customer.name} has successfully returned {dvd.name}"

