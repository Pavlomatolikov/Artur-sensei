import unittest

"""
    Develop a function that will take, start range,some input number, end range.
    It should return a list of numbers that contains an input digit.
    Don't use string methods
    Example:
        find_number(1, 5, 25) will return [5, 15, 25]
"""


def find_numbers(start, number, end):
  """
  implement me
  """
    pass


class Test(unittest.TestCase):
    def test_positive_find_numbers(self):
        assert find_numbers(0, 1, 150) == [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 31, 41, 51, 61, 71, 81, 91, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
        assert find_numbers(10, 9, 150) == [19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 109, 119, 129, 139, 149]
        assert find_numbers(5, 5, 150) == [5, 15, 25, 35, 45, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 65, 75, 85, 95, 105, 115, 125, 135, 145, 150]
        assert find_numbers(5, 5, 25) == [5, 15, 25]


if _name_ == '__main__':
    unittest.main()
