# tests/test_circle.py
import unittest
import math
from circle import area, perimeter


class CircleTestArea(unittest.TestCase):

    def test_area_1(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    def test_area_2(self):
        res = area(5)
        self.assertAlmostEqual(res, 25 * math.pi)

    def test_area_3(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_4(self):
        res = area(2)
        self.assertAlmostEqual(res, 4 * math.pi)

    def test_area_5(self):
        res = area(11)
        self.assertAlmostEqual(res, 121 * math.pi)

    def test_area_6(self):
        res = area(0.5)
        self.assertAlmostEqual(res, 0.25 * math.pi)

    def test_area_7(self):
        res = area(3)
        self.assertAlmostEqual(res, 9 * math.pi)

    def test_area_8(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25 * math.pi)

    def test_area_9(self):
        res = area(67)
        self.assertAlmostEqual(res, 4489 * math.pi)

    def test_area_10(self):
        res = area(-5)
        self.assertAlmostEqual(res, 'Длина радиуса не может быть отрицательной')
            

    def test_area_11(self):
        res = area(-882845938476953649)
        self.assertAlmostEqual(res, 'Длина радиуса не может быть отрицательной')

    def test_area_12(self):
        res = area(0.11)
        self.assertAlmostEqual(res, 0.0121 * math.pi)

    def test_area_13(self):
        res = area(1123)
        self.assertAlmostEqual(res, 1123 * 1123 * math.pi)

    def test_area_14(self):
        res = area('a')
        self.assertEqual(res, 'На вход было подано не число')


class CircleTestPerimeter(unittest.TestCase):

    def test_perimeter_1(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)

    def test_perimeter_2(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 10 * math.pi)

    def test_perimeter_3(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_4(self):
        res = perimeter(2)
        self.assertAlmostEqual(res, 4 * math.pi)

    def test_perimeter_5(self):
        res = perimeter(13)
        self.assertAlmostEqual(res, 26 * math.pi)

    def test_perimeter_6(self):
        res = perimeter(0.5)
        self.assertAlmostEqual(res, math.pi)

    def test_perimeter_7(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 7 * math.pi)

    def test_perimeter_8(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 5 * math.pi)

    def test_perimeter_9(self):
        res = perimeter(1.23)
        self.assertAlmostEqual(res, 2.46 * math.pi)

    def test_perimeter_10(self):
        res = perimeter(-5)
        self.assertAlmostEqual(res, 'Длина радиуса не может быть отрицательной')
            
    def test_perimeter_11(self):
        res = perimeter(-779766)
        self.assertAlmostEqual(res, 'Длина радиуса не может быть отрицательной')

    def test_perimeter_12(self):
        res = perimeter(0.132)
        self.assertAlmostEqual(res, 0.264 * math.pi)

    def test_perimeter_13(self):
        res = perimeter(99)
        self.assertAlmostEqual(res, 198 * math.pi)

    def test_perimeter_14(self):
        res = perimeter('a')
        self.assertEqual(res, 'На вход было подано не число')

