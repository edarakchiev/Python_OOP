class Customer:
    class_id = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_id()

    @classmethod
    def get_id(cls):
        cls.class_id = cls.class_id + 1
        return cls.class_id

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.class_id + 1


