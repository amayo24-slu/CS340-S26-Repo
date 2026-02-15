import unittest
from even_filter import get_evens

class TestEvenFilter(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_evens([]), [])

if __name__ == '__main__':
    unittest.main()