import unittest
from palindrome_checker import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

if __name__ == '__main__':
    unittest.main()