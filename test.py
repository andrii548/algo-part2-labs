import unittest
from lab5 import flood_fill

class TestFloodFill(unittest.TestCase):
    def test_basic_flood_fill(self):
        test_mat =[
            ['Y', 'Y', 'G', 'G'],
            ['Y', 'Y', 'G', 'X'],
            ['G', 'G', 'G', 'X'],
            ['W', 'W', 'W', 'X']
        ]
        
        expected = [
            ['Y', 'Y', 'C', 'C'],
            ['Y', 'Y', 'C', 'X'],
            ['C', 'C', 'C', 'X'],
            ['W', 'W', 'W', 'X']
        ]
        
        result = flood_fill(test_mat, 4, 4, 0, 3, 'C')
        self.assertEqual(result, expected)

    def test_same_color_replacement(self):
      
        test_mat =[
            ['Y', 'Y', 'G', 'G'],
            ['Y', 'Y', 'G', 'X'],
            ['G', 'G', 'G', 'X'],
            ['W', 'W', 'W', 'X']
        ]
        
        result = flood_fill(test_mat, 4, 4, 0, 0, 'Y')
        self.assertEqual(result, test_mat)

    def test_out_of_bounds(self):
        test_mat =[
            ['Y', 'Y', 'G', 'G'],
            ['Y', 'Y', 'G', 'X'],
            ['G', 'G', 'G', 'X'],
            ['W', 'W', 'W', 'X']
        ]
        
        with self.assertRaises(IndexError):
            flood_fill(test_mat, 4, 4, 10, 10, 'C')

    def test_isolated_cell(self):
        isolated_matrix = [
            ['B', 'B', 'B'],
            ['B', 'A', 'B'],
            ['B', 'B', 'B']
        ]
        
        expected = [
            ['B', 'B', 'B'],
            ['B', 'Z', 'B'], 
            ['B', 'B', 'B']
        ]
        
        result = flood_fill(isolated_matrix, 3, 3, 1, 1, 'Z')
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()