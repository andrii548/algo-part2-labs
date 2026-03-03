import unittest
from lab2 import hamster_count


class TestLab2(unittest.TestCase):

    def test_1(self):
        s = 7
        c = 3
        hamster_list = [[1, 2], [2, 2], [3, 1]]

        expected = 2

        self.assertEqual(hamster_count(s, c, hamster_list ), expected)

    def test_2(self):
        s = 19
        c = 4
        hamster_list = [[5, 0], [2, 2], [1, 4], [5, 1]]

        expected = 3

        self.assertEqual(hamster_count(s, c, hamster_list ), expected)

    def test_3(self):
        s = 2
        c = 2
        hamster_list = [[1, 50000], [1, 60000]]

        expected = 1

        self.assertEqual(hamster_count(s, c, hamster_list ), expected)

    def test_4(self):
        s = 32
        c = 3
        hamster_list = [[1,2], [3, 4], [5,6]]

        expected = 2

        self.assertEqual(hamster_count(s, c, hamster_list ), expected)
        



if __name__ == "__main__":
    unittest.main()