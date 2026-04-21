import unittest
from lab6 import min_beer_types


class TestBeerParty(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(min_beer_types(2, 2, "YN NY"), 2)

    def test_example_2(self):
        self.assertEqual(min_beer_types(6, 3, "YNN YNY YNY NYY NYY NYN"), 2)

    def test_all_like_one(self):
        self.assertEqual(min_beer_types(3, 3, "YNN YNN YNN"), 1)

    def test_unique_tastes(self):
        self.assertEqual(min_beer_types(3, 3, "YNN NYN NNY"), 3)

    def test_complex_overlap(self):
        self.assertEqual(min_beer_types(3, 3, "YNY YYN NYY"), 2)


if __name__ == '__main__':
    unittest.main()