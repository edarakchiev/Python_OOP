import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    name = "test_name"
    type = "test_type"
    sound = "test_sound"

    def setUp(self):
        self.mammal = Mammal(self.name, self.type, self.sound)

    def test_init_method(self):
        pass

    def test_init_method__name(self):
        self.assertEqual(self.name, self.mammal.name)

    def test_init_method__type(self):
        self.assertEqual(self.type, self.mammal.type)

    def test_init_method__sound(self):
        self.assertEqual(self.sound, self.mammal.sound)

    def test_make_sound_method(self):
        actual = self.mammal.make_sound()
        expected = f"{self.name} makes {self.sound}"
        self.assertEqual(actual, expected)

    def test_initial_kingdom(self):
        actual = self.mammal._Mammal__kingdom
        self.assertEqual(actual, "animals")

    def test_get_kingdom_method(self):
        actual = self.mammal.get_kingdom()
        expected = "animals"
        self.assertEqual(actual, expected)

    def test_info_method(self):
        actual = self.mammal.info()
        expected = f"{self.name} is of type {self.type}"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()