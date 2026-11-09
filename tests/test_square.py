# tests/test_square.py
import unittest
from square import area, perimeter


class SquareTestArea(unittest.TestCase):

    def test_area_1(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_2(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_3(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_4(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_area_5(self):
        res = area(11)
        self.assertEqual(res, 121)

    def test_area_6(self):
        res = area(1000)
        self.assertEqual(res, 1000000)

    def test_area_7(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_area_8(self):
        res = area(0.1)
        self.assertAlmostEqual(res, 0.01)

    def test_area_9(self):
        res = area(1.5)
        self.assertEqual(res, 2.25)

    def test_area_10(self):
        res = area(-67)
        self.assertEqual(res, 'Длины сторон не могут быть отрицательными')

    def test_area_11(self):
        res = area(12434123)
        self.assertEqual(res, 154607414779129)

    def test_area_12(self):
        res = area(228)
        self.assertEqual(res, 51984)

    def test_area_13(self):
        res = area(-3.234761379239888)
        self.assertEqual(res, 'Длины сторон не могут быть отрицательными')

    def test_area_15(self):
        res = area(7.1)
        self.assertEqual(res, 50.41)

    def test_area_16(self):
        res = area('a')
        self.assertEqual(res, 'На вход было подано не число')


class SquareTestPerimeter(unittest.TestCase):

    def test_perimeter_1(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_2(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimeter_3(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_4(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_perimeter_5(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_6(self):
        res = perimeter(228)
        self.assertEqual(res, 912)

    def test_perimeter_7(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10.0)

    def test_perimeter_8(self):
        res = perimeter(0.1)
        self.assertAlmostEqual(res, 0.4)

    def test_perimeter_9(self):
        res = perimeter(1.5)
        self.assertEqual(res, 6.0)

    def test_perimeter_10(self):
        res = perimeter(-5)
        self.assertEqual(res, 'Длины сторон не могут быть отрицательными')

    def test_perimeter_11(self):
        res = perimeter(-7646367473.98435938478)
        self.assertEqual(res, 'Длины сторон не могут быть отрицательными')

    def test_perimeter_12(self):
        res = perimeter(4.6752)
        self.assertEqual(res, 18.7008)

    def test_perimeter_13(self):
        res = perimeter(3.21)
        self.assertEqual(res, 12.84)

    def test_perimeter_14(self):
        res = perimeter('a')
        self.assertEqual(res, 'На вхож было подано не число')

