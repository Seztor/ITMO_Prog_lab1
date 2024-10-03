import unittest
from src.lab1_1.calculator import to_calc


class CalculatorTestCase(unittest.TestCase):

    def test_calc_one(self):
        self.assertEqual(float(to_calc('2+2*2')), float(6))

    def test_calc_two(self):
        self.assertEqual(float(to_calc('(8*2)+(6/3)')), float(18))

    def test_calc_three(self):
        self.assertEqual(float(to_calc('(1*2*3*4)-1234')), float(-1210))

    def test_calc_four(self):
        self.assertEqual(float(to_calc('2^4/2^2')), float(4))

    def test_calc_five(self):
        self.assertEqual(float(to_calc('4/(2/4)')), float(8))

    def test_calc_six(self):
        self.assertEqual(float(to_calc('1/3^2')), float(1/9))

    def test_calc_seven(self):
        self.assertEqual(float(to_calc('(1+2)*(3/2)')), float(4.5))

    def test_calc_eight(self):
        self.assertEqual(float(to_calc('64^0.5')), float(8))