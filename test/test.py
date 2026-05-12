import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from lab9 import find_occurrences


class TestFiniteAutomaton(unittest.TestCase):
    def test_single_match(self):
        self.assertEqual(find_occurrences("привіт світ", "світ"), [7])

    def test_multiple_matches(self):
        self.assertEqual(find_occurrences("abababa", "aba"), [0, 2, 4])

    def test_no_match(self):
        self.assertEqual(find_occurrences("hello world", "python"), [])

    def test_empty_needle(self):
        self.assertEqual(find_occurrences("hello", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(find_occurrences("", "hello"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(find_occurrences("hi", "hello"), [])

    def test_all_same_characters(self):
        self.assertEqual(find_occurrences("aaaaa", "aa"), [0, 1, 2, 3])


if __name__ == "__main__":
    unittest.main()