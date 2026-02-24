import unittest
from fridge import check_temperature

class TestFridge(unittest.TestCase):

    def test_temperature_rising(self):
        result = check_temperature([1, 2, 3, 4, 5])
        self.assertEqual(result, "Error: temperature rises")

    def test_temperature_jumping(self):
        result = check_temperature([2, 4, 2, 5, 3])
        self.assertEqual(result, "The temperature is normal")

    def test_temperature_cooling(self):
        result = check_temperature([5, 4, 3, 2, 1])
        self.assertEqual(result, "The temperature is normal")

if __name__ == '__main__':
    unittest.main()