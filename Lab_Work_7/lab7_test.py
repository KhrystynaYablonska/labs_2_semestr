import unittest
import os
import csv
from lab7 import calculate_minimum_cable

class TestMinimumCable(unittest.TestCase):

    def create_test_csv(self, filename, data):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def test_successful_connection(self):
        filename = 'test_success.csv'
        data = [
            ['K1', 'K2', '2000'],
            ['K2', 'K3', '1000'],
            ['K1', 'K3', '4000'],
            ['K3', 'K4', '500']
        ]
        self.create_test_csv(filename, data)
        self.assertEqual(calculate_minimum_cable(filename), 3500)
        os.remove(filename)

    def test_disconnected_wells(self):
        filename = 'test_fail.csv'
        data = [
            ['K1', 'K2', '2000'],
            ['K3', 'K4', '1500']
        ]
        self.create_test_csv(filename, data)
        self.assertEqual(calculate_minimum_cable(filename), -1)
        os.remove(filename)

    def test_single_path(self):
        filename = 'test_single.csv'
        data = [
            ['K1', 'K2', '100']
        ]
        self.create_test_csv(filename, data)
        self.assertEqual(calculate_minimum_cable(filename), 100)
        os.remove(filename)

    def test_missing_file(self):
        self.assertEqual(calculate_minimum_cable('non_existent_file.csv'), -1)

if __name__ == '__main__':
    unittest.main()