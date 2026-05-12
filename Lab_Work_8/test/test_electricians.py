import unittest
import sys
import os

# Додаємо шлях до папки src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.src_electricians import calculate_max_wire_length

class TestElectricians(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(calculate_max_wire_length(2, [3, 3, 3]), 5.66)

    def test_example_2(self):
        self.assertEqual(calculate_max_wire_length(100, [1, 1, 1, 1]), 300.0)

    def test_example_3(self):
        self.assertEqual(calculate_max_wire_length(4, [100, 2, 100, 2, 100]), 396.32)

if __name__ == '__main__':
    unittest.main()