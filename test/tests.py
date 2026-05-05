import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab8 import solve


class TestIJones(unittest.TestCase):

    def run_test_case(self, input_data: str, expected_output: int):
        with open('ijones.in', 'w', encoding='utf-8') as f:
            f.write(input_data)

        solve()

        with open('ijones.out', 'r', encoding='utf-8') as f:
            result = f.read().strip()

        self.assertEqual(int(result), expected_output)

    def test_example_1(self):
        input_data = (
            "3 3\n"
            "aaa\n"
            "cab\n"
            "def\n"
        )
        self.run_test_case(input_data, 5)

    def test_example_2(self):
        input_data = (
            "10 1\n"
            "abcdefaghi\n"
        )
        self.run_test_case(input_data, 2)

    def test_example_3(self):
        input_data = (
            "7 6\n"
            "aaaaaaa\n"
            "aaaaaaa\n"
            "aaaaaaa\n"
            "aaaaaaa\n"
            "aaaaaaa\n"
            "aaaaaaa\n"
        )
        self.run_test_case(input_data, 201684)

    def tearDown(self):
        if os.path.exists('ijones.in'):
            os.remove('ijones.in')
        if os.path.exists('ijones.out'):
            os.remove('ijones.out')


if __name__ == '__main__':
    unittest.main()