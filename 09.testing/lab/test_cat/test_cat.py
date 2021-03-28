import unittest
from cat.cat import Cat


class CatTests(unittest.TestCase):
    name = "Vanesa"

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_size__increased__after_eating(self):
        '''Cat's size is increased after eating'''
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed__after_eating(self):
        '''Cat is fed after eating'''
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed__expected_error(self):
        '''Cat cannot eat if already fed, raises an error'''
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


    def test_cat_cannot_fall_assleep_if_not_fed__excepted_error(self):
        '''Cat cannot fall asleep if not fed, raises an error'''
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_not_sleepy_after_sleeping(self):
        '''Cat is not sleepy after sleeping'''

        with self.assertRaises(Exception):
            self.cat.sleep()


if __name__ == '__main__':
    unittest.main()