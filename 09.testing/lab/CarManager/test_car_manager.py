import unittest
from car_manager import Car


class CarTests(unittest.TestCase):
    make = 'test_make'
    model = 'test_model'
    fuel_consumption = 7
    fuel_capacity = 70

    def test_car_make_setter__when_data_is_correct__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual(car.make, "test_make")

    def test_car_make_setter__when_None__expect_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.make = None

    def test_model_getter(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        self.assertEqual(car.model, "test_model")

    def test_model_setter_when_data_is_correct(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.model = "BMW"
        self.assertEqual(car.model, "BMW")

    def test_model_setter__with_empty_data__expected_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.model = None

    def test_fuel_consumption_with_correct_data(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_consumption = 8
        self.assertEqual(car.fuel_consumption, 8)

    def test_fuel_consumption__when_negative_value__expected_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_consumption = -7

    def test_fuel_capacity__with_correct_data(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_capacity = 100
        self.assertEqual(car.fuel_capacity, 100)

    def test_fuel_capacity_when_capacity_is_negative__expected_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_capacity = -100

    def test_fuel_amount__when_data_is_correct(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 70
        self.assertEqual(car.fuel_amount, 70)

    def test_fuel_amount__when_amount_is_negative_value__expected_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.fuel_amount = -7

    def test_refuel_method__when_data_is_correct__expected_executed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(7)
        self.assertEqual(7, car.fuel_amount)

    def test_refuel_method__when_refuel_value_is_biggest_from_capacity__expected_refuel_with_capacity(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.refuel(77)
        self.assertEqual(70, car.fuel_amount)

    def test_refuel_method__when_refuel_value_is_negative__expected_exception(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        with self.assertRaises(Exception):
            car.refuel(-7)

    def test_drive_method__when_fuel_is_enough__expected_executed(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 37
        car.drive(100)
        self.assertEqual(30, car.fuel_amount)

    def test_drive_method__when_do_not_have_enough_fuel__expected_exceprtion(self):
        car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)
        car.fuel_amount = 7
        with self.assertRaises(Exception):
            car.drive(101)

if __name__ == '__main__':
    unittest.main()