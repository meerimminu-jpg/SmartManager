import unittest
from main import add, divide, is_even

class TestMyCode(unittest.TestCase):

    # Кошууну текшерүү
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    # Бөлүүнү текшерүү
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        # Катаны текшерүү (exception)
        with self.assertRaises(ValueError):
            divide(10, 0)

    # Жуп санды текшерүү
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))

if __name__ == '__main__':
    unittest.main()


