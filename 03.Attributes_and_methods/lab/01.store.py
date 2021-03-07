class Store:
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        self.items_counter = 0

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

    @classmethod
    def from_size(cls, name, type, size):
        return cls(name, type, size //2)

    @staticmethod
    def can_add_item(capacity, counter):
        return counter < capacity

    @staticmethod
    def can_remove_item(items, item_name, amount):
        return item_name in items and amount <= items[item_name]



    def add_item(self, item_name):
        if not self.can_add_item:
            return "Not enough capacity in the store"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        self.items_counter += 1
        return f"{item_name} added to the store"

    def remove_item(self, item_name, amount):
        if not self.can_remove_item(self.items, item_name, amount):
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount
        self.items_counter -= amount
        return f"{amount} {item_name} removed from the store"


first_store = Store("First store", "Fruit and Veg", 20)
second_store = Store.from_size("Second store", "Clothes", 500)

print(first_store)
print(second_store)

print(first_store.add_item("potato"))
print(second_store.add_item("jeans"))
print(first_store.remove_item("tomatoes", 1))
print(second_store.remove_item("jeans", 1))
