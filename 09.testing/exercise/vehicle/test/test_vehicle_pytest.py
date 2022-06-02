import pytest
from project.vehicle import Vehicle


def init_test_vehicle(fuel=70, horse_power=100):
    return Vehicle(fuel, horse_power)


class TestVehicle:
    def test_init_method(self):
        test_vehicle = init_test_vehicle()
        assert test_vehicle.fuel == 70
        assert test_vehicle.capacity == 70
        assert test_vehicle.fuel_consumption == 1.25
        assert test_vehicle.horse_power == 100

    def test_fuel(self):
        test_vehicle = init_test_vehicle()
        assert test_vehicle.capacity == 70
        assert test_vehicle.fuel_consumption == 1.25
        assert test_vehicle.horse_power == 100

    def test_vehicle_drive_when_fuel_is_enough(self):
        test_vehicle = init_test_vehicle()
        test_vehicle.drive(10)
        assert test_vehicle.fuel == 57.5

    def test_vehicle_drive_when_fuel_not_enough(self):
        test_vehicle = init_test_vehicle()
        with pytest.raises(Exception) as ex:
            test_vehicle.drive(90)
        assert "Not enough fuel" == str(ex.value)

    def test_refuel_with_enough_fuel(self):
        test_vehicle = init_test_vehicle()
        test_vehicle.fuel = 20
        test_vehicle.refuel(30)
        assert test_vehicle.fuel == 50

    def test_refuel_with_to_much_fuel(self):
        test_vehicle = init_test_vehicle()
        with pytest.raises(Exception) as ex:
            test_vehicle.refuel(30)
        assert "Too much fuel" == str(ex.value)

    def test_str_vehicle(self):
        test_vehicle = init_test_vehicle()
        expected_message = f"The vehicle has 100 horse power with 70 fuel left and 1.25 fuel consumption"
        assert test_vehicle.__str__() == expected_message
