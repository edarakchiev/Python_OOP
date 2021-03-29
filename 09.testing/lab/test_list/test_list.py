import unittest
from integer_list.integer_list import IntegerList


class TestList(unittest.TestCase):

    def test_add_operation__with_int(self):
        my_list = IntegerList()
        my_list = my_list.add(7)
        self.assertEqual(my_list, [7])

    def test_add_operation__with_str__expected_error(self):
        my_list = IntegerList()
        with self.assertRaises(ValueError):
            my_list.add("E")

    def test_remove_index__with_correct_index(self):
        my_list = IntegerList(1, 2, 3, 4)
        expected = 3
        actual = my_list.remove_index(2)
        self.assertEqual(expected, actual)

    def test_remove_index__index_biggest__expected_error(self):
        my_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            my_list.remove_index(4)

    def test_remove_index__index_negative__expected_error(self):
        my_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError):
            my_list.remove_index(-5)

    def test_get_method__with_correct_index(self):
        my_list = IntegerList(1, 2, 3)
        actual = my_list.get(1)
        expected = 2
        self.assertEqual(actual, expected)

    def test_insert_method_with_index_in_range(self):
        my_list = IntegerList(1, 2, 3)
        my_list.insert(0, 7)
        actual = my_list.get_data()
        expected = [7, 1, 2, 3]
        self.assertEqual(actual, expected)

    def test_get_method__with_negative_index__out_of_range(self):
        my_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            my_list.get(-4)

    def test_get_method__with_positive_index__out_of_range(self):
        my_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            my_list.get(3)

    def test_insert_method__with_index_out_of_range__el_is_int__expected_error(self):
        my_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError):
            my_list.insert(4, 7)

    def test_insert_method__with_index_in_range__el_is_not_int__expected_error(self):
        my_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError):
            my_list.insert(2, 'element')

    def test_get_biggest(self):
        my_list = IntegerList(1, 2, 3, 7)
        expected = my_list.get_biggest()
        self.assertEqual(7, expected)

    def test_get_index(self):
        my_list = IntegerList(1, 2, 3, 7)
        expected = my_list.get_index(7)
        self.assertEqual(3, expected)

    def test_init_constructor(self):
        my_list = IntegerList(1, 2, 3, 4)
        self.assertEqual([1, 2, 3, 4], my_list.get_data())


if __name__ == '__main__':
    unittest.main()
