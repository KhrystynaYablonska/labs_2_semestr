import unittest
import os
from lab5 import min_knight_moves, main

class TestKnightPath(unittest.TestCase):

    def test_min_knight_moves(self):
        self.assertEqual(min_knight_moves(8, (7, 0), (0, 7)), 6)
        self.assertEqual(min_knight_moves(8, (0, 0), (0, 0)), 0)
        self.assertEqual(min_knight_moves(8, (0, 0), (2, 1)), 1)

    def test_io_files(self):
        with open('input.txt', 'w', encoding='utf-8') as f:
            f.write("8 # розмір поля\n")
            f.write("7, 0 # стартова точка\n")
            f.write("0, 7 # точка призначення\n")

        main()

        with open('output.txt', 'r', encoding='utf-8') as f:
            result = f.read().strip()

        self.assertEqual(result, "6")

    def tearDown(self):
        if os.path.exists('input.txt'):
            os.remove('input.txt')
        if os.path.exists('output.txt'):
            os.remove('output.txt')

if __name__ == '__main__':
    unittest.main()