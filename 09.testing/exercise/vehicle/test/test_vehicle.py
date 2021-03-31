from project.vehicle import Vehicle
import unittest


class VehicleTest(unittest.TestCase):
    fuel = 70
    horse_power = 150

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_init_method(self):
        self.assertEqual(self.vehicle.fuel, self.fuel)
        self.assertEqual(self.vehicle.capacity, self.fuel)
        self.assertEqual(self.vehicle.horse_power, self.horse_power)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_method__when_fuel_is_not_enough__expected_exception(self):
        with self.assertRaises(Exception) as exp:
            self.vehicle.drive(700)
        expected = "Not enough fuel"
        self.assertEqual(exp.exception.args[0], expected)

    def test_drive_method__when_fuel_is_enough__expected_execute(self):
        self.vehicle.drive(10)
        actual = self.vehicle.fuel
        expected = 57.5
        self.assertEqual(actual, expected)

    def test_refuel_method__when_fuel_is_too_much__expected_exception(self):
        with self.assertRaises(Exception) as exp:
            self.vehicle.refuel(10)
        expected = "Too much fuel"
        self.assertEqual(exp.exception.args[0], expected)

    def test_refuel_method__when_fuel_is_enough_expected_execute(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(10)
        actual = self.vehicle.fuel
        expected = 60
        self.assertEqual(actual, expected)

    def test_str_method(self):
        actual = self.vehicle.__str__()
        expected = f"The vehicle has 150 horse power with 70 fuel left and 1.25 fuel consumption"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()