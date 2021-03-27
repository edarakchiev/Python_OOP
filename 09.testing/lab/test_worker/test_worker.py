import unittest
from worker.worker import Worker


class WorkerTests(unittest.TestCase):
    name = "Test Worker"
    salary = 1000
    energy = 5

    def setUp(self):
        self.worker = Worker(self.name, self.salary, self.energy)

    def test_worker__when_correct_args__expect_to_be_initialized(self):
        '''Test if the worker is initialized with correct name, salary and energy'''
        self.assertEqual(self.name, self.worker.name)
        self.assertEqual(self.salary, self.worker.salary)
        self.assertEqual(self.energy, self.worker.energy)

    def test_workers_rest__expected_to_be_incremented(self):
        '''Test if the worker's energy is incremented after the rest method is called'''
        self.worker.rest()
        self.assertEqual(self.energy + 1, self.worker.energy)

    def test_worker_work__when_energy_is_0__expected_exception(self):
        '''Test if an error is raised if the worker tries to work with negative energy or equal to 0'''
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_workers_money__increased_by_salary_after_work_called(self):
        '''Test if the worker's money is increased by his salary correctly after the work method is called'''
        self.worker.work()
        self.assertEqual(self.salary, self.worker.money)

    def test_worker_energy_after_work_called(self):
        '''Test if the worker's energy is decreased after the work method is called'''
        self.worker.work()
        self.assertEqual(self.energy - 1, self.worker.energy)

    def test_worker_get_info(self):
        '''Test if the get_info method returns the proper string with correct value'''
        actual_info = self.worker.get_info()
        expected_info = f'{self.name} has saved 0 money.'
        self.assertEqual(actual_info, expected_info)


if __name__ == '__main__':
    unittest.main()

