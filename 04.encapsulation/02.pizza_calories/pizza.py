class Pizza:
    def __init__(self, name, dough, topping_capacity):
        self.__name = name
        self.__dough = dough
        self.__toppings_capacity = topping_capacity
        self.__toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, new_dough):
        self.__dough = new_dough

    @property
    def topping_capacity(self):
        return self.__toppings_capacity

    @topping_capacity.setter
    def topping_capacity(self, new_toppings_capacity):
        self.__toppings_capacity = new_toppings_capacity

    @property
    def toppings(self):
        return self.__toppings

    # @toppings.setter
    # def toppings(self, key, value):
    #     self.__toppins[key] = value
    #     return self.__toppings

    def add_topping(self, topping):
        if self.__toppings_capacity == len(self.toppings):
            raise ValueError("Not enough space for another topping")
        key = topping.topping_type
        value = topping.weight
        if key not in self.toppings:
            self.__toppings[key] = 0
        self.__toppings[key] += value
        # self.toppings(key, value)

    def calculate_total_weight(self):
        result = 0
        for weight in self.toppings.values():
            result += weight
        result += self.dough.weight
        return result
