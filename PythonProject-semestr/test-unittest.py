import unittest
from generator import is_prime

class TestPrimeFunctions(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))


if __name__ == '__main__':
    unittest.main()

