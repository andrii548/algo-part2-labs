import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from lab6 import solve

class TestGamsrv(unittest.TestCase):
    
    def run_test_with_data(self, input_data, expected_output):
        with open('gamsrv.in', 'w') as f:
            f.write(input_data)      
        solve() 
        with open('gamsrv.out', 'r') as f:
            result = f.read().strip()
            
        self.assertEqual(result, str(expected_output))

    def test_1(self):
        input_data = """
        6 6\n
        1 2 6\n
        1 3 10\n
        3 4 80\n
        4 5 50\n
        5 6 20\n
        2 3 40\n
        2 4 100"""
        self.run_test_with_data(input_data, 100)

    def test_2(self):
        input_data = """
        9 12\n
        2 4 6\n
        1 2 20\n
        2 3 20\n
        3 6 20\n
        6 9 20\n
        9 8 20\n
        8 7 20\n
        7 4 20\n
        4 1 20\n
        5 2 10\n
        5 4 10\n
        5 6 10\n
        5 8 10"""
        self.run_test_with_data(input_data, 10)

    def test_3(self):
        input_data = """
        3 2\n
        1 3\n
        1 2 50\n
        2 3 1000000000"""
        self.run_test_with_data(input_data, 1000000000)

    def tearDown(self):
        if os.path.exists('gamsrv.in'):
            os.remove('gamsrv.in')
        if os.path.exists('gamsrv.out'):
            os.remove('gamsrv.out')

if __name__ == '__main__':
    unittest.main()