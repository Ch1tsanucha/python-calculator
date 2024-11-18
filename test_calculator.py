import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_negative_add(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)

    def test_negative_multiply(self):
        self.assertEqual(self.calc.multiply(-1, -2), 2)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2, 2), 1)

    def test_zero_divide(self):
        self.assertEqual(self.calc.divide(1, 0), 0)

    # Test for modulo
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(2, 4), 2) 

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(5, 0), 0)  


if __name__ == '__main__':
    unittest.main()
