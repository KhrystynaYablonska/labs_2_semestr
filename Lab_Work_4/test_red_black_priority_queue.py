import unittest
from red_black_priority_queue import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("Task 1", 10)
        self.assertEqual(self.pq.peek(), {"value": "Task 1", "priority": 10})

        self.pq.insert("Task 2", 20)
        self.assertEqual(self.pq.peek(), {"value": "Task 2", "priority": 20})

        self.pq.insert("Task 3", 5)
        self.assertEqual(self.pq.peek(), {"value": "Task 2", "priority": 20})

    def test_extract_max(self):
        self.pq.insert("Low", 1)
        self.pq.insert("High", 100)
        self.pq.insert("Medium", 50)

        self.assertEqual(self.pq.extract_max(), {"value": "High", "priority": 100})
        self.assertEqual(self.pq.extract_max(), {"value": "Medium", "priority": 50})
        self.assertEqual(self.pq.extract_max(), {"value": "Low", "priority": 1})
        self.assertIsNone(self.pq.extract_max())

    def test_equal_priorities(self):
        self.pq.insert("A", 10)
        self.pq.insert("B", 10)
        self.pq.insert("C", 10)

        res1 = self.pq.extract_max()
        res2 = self.pq.extract_max()
        res3 = self.pq.extract_max()

        self.assertEqual(res1["priority"], 10)
        self.assertEqual(res2["priority"], 10)
        self.assertEqual(res3["priority"], 10)
        self.assertIsNone(self.pq.extract_max())

    def test_empty_queue(self):
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.extract_max())

if __name__ == '__main__':
    unittest.main()