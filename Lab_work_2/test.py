import unittest
from nanosoft import find_min_board

class TestBoardSize(unittest.TestCase):
    def test_example_from_task(self):
        self.assertEqual(find_min_board(2, 3, 10), 9)

    def test_single_leaf(self):
        self.assertEqual(find_min_board(1, 1, 1), 1)

    def test_square_leaves(self):
        self.assertEqual(find_min_board(2, 2, 4), 4)

    if __name__ == '__main__':
        unittest.main()