import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lab6 import max_experience_with_path

class TestCareer(unittest.TestCase):
    def test_example1(self):
        levels = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1]
        ]
        experience, _ = max_experience_with_path(levels)
        self.assertEqual(experience, 12)

    def test_example2(self):
        levels = [
            [9999]
        ]
        experience, _ = max_experience_with_path(levels)
        self.assertEqual(experience, 9999)

    def test_example3(self):
        levels = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]
        experience, _ = max_experience_with_path(levels)
        self.assertEqual(experience, 3)

    def test_single_zero(self):
        levels = [
            [0]
        ]
        experience, _ = max_experience_with_path(levels)
        self.assertEqual(experience, 0)

    def test_large_simple(self):
        levels = [list(range(1, i + 2)) for i in range(1000)]
        expected = sum(i + 1 for i in range(1000))
        experience, _ = max_experience_with_path(levels)
        self.assertEqual(experience, expected)

if __name__ == '__main__':
    unittest.main()
