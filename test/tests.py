import unittest
import os
import sys
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from lab7 import solve

class TestIslandsMST(unittest.TestCase):

    def setUp(self):
        self.test_filename = 'test_islands.csv'

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def create_csv_file(self, data):
        with open(self.test_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data)

    def test_connected_graph(self):
        matrix = [
            [0, 2, 0, 6],
            [2, 0, 3, 8],
            [0, 3, 0, 5],
            [6, 8, 5, 0]
        ]
        self.create_csv_file(matrix)
        result = solve(self.test_filename)
        self.assertEqual(result, 10.0)

    def test_single_island(self):
        matrix = [[0]]
        self.create_csv_file(matrix)
        result = solve(self.test_filename)
        self.assertEqual(result, 0.0)

    def test_disconnected_graph(self):
        matrix = [
            [0, 4, 0],
            [4, 0, 0],
            [0, 0, 0]  
        ]
        self.create_csv_file(matrix)
        result = solve(self.test_filename)
        self.assertEqual(result, 4.0)

    def test_empty_cells(self):
        matrix = [
            [0, 5, ""],
            [5, 0, 7],
            ["", 7, 0]
        ]
        self.create_csv_file(matrix)
        result = solve(self.test_filename)
        self.assertEqual(result, 12.0)

if __name__ == '__main__':
    unittest.main()