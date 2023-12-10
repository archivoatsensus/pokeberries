import unittest

from utils import calculate_median, calculate_variance


class TestUtils(unittest.TestCase):
    def test_calculate_median(self):
        odd_list = [5, 9, 11, 9, 7]
        even_list = [2, 5, 1, 4, 2, 7]
        decimal_median_list = [1, 2, 1, 2, 1, 2]

        self.assertEqual(9, calculate_median(odd_list))
        self.assertEqual(3, calculate_median(even_list))
        self.assertEqual(1.5, calculate_median(decimal_median_list))

    def test_calculate_variance(self):
        list_a = [3, 5, 8, 1]
        list_b = [50, 55, 45, 60, 40]

        self.assertEqual(6.6875, calculate_variance(list_a))
        self.assertEqual(50, calculate_variance(list_b))


if __name__ == '__main__':
    unittest.main()
