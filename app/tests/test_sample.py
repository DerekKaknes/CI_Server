import unittest

from app.code.sample import add, is_prime, cubed


class SampleTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(91))
        self.assertFalse(is_prime(97**2))

    def test_cubed(self):
        self.assertEqual(cubed(3), 27)
        self.assertEqual(cubed(1), 1)
        self.assertEqual(cubed(-5), -125)
