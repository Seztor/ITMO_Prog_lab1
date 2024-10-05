import unittest
from src.lab1_1.calculator import to_calc, get_split_arr




class CalculatorTestCase(unittest.TestCase):

    def test_calc_1(self):
        self.assertEqual(to_calc('2+2*2'), round(float(6),7))

    def test_calc_2(self):
        self.assertEqual(to_calc('(8*2)+(6/3)'), round(float(18),7))

    def test_calc_3(self):
        self.assertEqual(to_calc('(1*2*3*4)-1234'), round(float(-1210),7))

    def test_calc_4(self):
        self.assertEqual(to_calc('2^4/2^2'), round(float(4),7))

    def test_calc_5(self):
        self.assertEqual(to_calc('4/(2/4)'), round(float(8),7))

    def test_calc_6(self):
        self.assertEqual(to_calc('1/3^2'), round(float(1/9),7))

    def test_calc_7(self):
        self.assertEqual(to_calc('(1+2)*(3/2)'), round(float(4.5),7))

    def test_calc_8(self):
        self.assertEqual(to_calc('64^0.5'), round(float(8),7))

    def test_calc_9(self):
        self.assertEqual(to_calc('1/0'), 'Error: Division by zero')

    def test_calc_10(self):
        self.assertEqual(to_calc('0.1 + 0.2'), round(float(0.3),7))

    def test_calc_11(self):
        self.assertEqual(to_calc('1+3-'), 'Input Error')
