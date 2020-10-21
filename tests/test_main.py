import unittest

import sys
sys.path.append("src")

from main import Factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_0(self):
        self.assertEqual(Factorial(0).result, 1, "Should be 1")

    def test_factorial_1_or_higher(self):
        self.assertEqual(Factorial(1).result, 1, "Should be 1")
        self.assertEqual(Factorial(2).result, 2, "Should be 2")
        self.assertEqual(Factorial(3).result, 6, "Should be 6")
        self.assertEqual(Factorial(10).result, 3628800, "Should be 3628800")

if __name__ == '__main__':
    unittest.main()

