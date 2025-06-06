import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from lab7 import boyer_moore_search


class TestBoyerMooreSearch(unittest.TestCase):
    def test_single_match(self):
        self.assertEqual(boyer_moore_search("hello world", "world"), [6])

    def test_multiple_matches(self):
        self.assertEqual(boyer_moore_search("abcabcabc", "abc"), [0, 3, 6])

    def test_no_match(self):
        self.assertEqual(boyer_moore_search("abcdef", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(boyer_moore_search("abcdef", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(boyer_moore_search("", "abc"), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(boyer_moore_search("abc", "abcdef"), [])


if __name__ == "__main__":
    unittest.main()
