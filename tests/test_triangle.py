# tests/test_triangle.py
import unittest
from triangle import area, perimeter


class TriangleTestArea(unittest.TestCase):

    def test_area_1(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_area_2(self):
        res = area(6, 4)
        self.assertEqual(res, 12)

    def test_area_3(self):
        res = area(1, 1)
        self.assertEqual(res, 0.5)

    def test_area_4(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_5(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_6(self):
        res = area(100, 50)
        self.assertEqual(res, 2500)

    def test_area_7(self):
        res = area(2.5, 4)
        self.assertEqual(res, 5.0)

    def test_area_8(self):
        res = area(1.5, 3)
        self.assertEqual(res, 2.25)

    def test_area_9(self):
        res = area(3, 2.5)
        self.assertEqual(res, 3.75)

    def test_area_10(self):
        res = area(-10, 5)
        self.assertEqual(res, 'Длины сторон не могут быть отрицательными')

    def test_area_11(self):
        res = area(-1123123, -1341234123)
        self.assertEqual(res, 'Длины сторон не могут быть отрицательными')

    def test_area_12(self):
        res = area(0.1, 0.2)
        self.assertAlmostEqual(res, 0.01)

    def test_area_13(self):
        res = area(7, 7)
        self.assertEqual(res, 24.5)

    def test_area_14(self):
        res = area('a', 1)
        self.assertEqual(res, 'На вход было подано не число')

    def test_area_14(self):
        res = area('a', 'b')
        self.assertEqual(res, 'На вход было подано не число')

    def test_area_14(self):
        res = area(1, 'a')
        self.assertEqual(res, 'На вход было подано не число')
    


class TriangleTestPerimeter(unittest.TestCase):

    def test_perimeter_1(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_2(self):
        res = perimeter(6, 6, 6)
        self.assertEqual(res, 18)

    def test_perimeter_3(self):
        res = perimeter(5, 12, 13)
        self.assertEqual(res, 30)

    def test_perimeter_4(self):
        res = perimeter(67, 52, 42)
        self.assertEqual(res, 161)
    
    def test_perimeter_4(self):
        res = perimeter(67, -52, -42)
        self.assertEqual(res, 'Длины не могут быть отрицательными')

    def test_perimeter_5(self):
        res = perimeter(-12, 11412, -1)
        self.assertEqual(res, 'Длины не могут быть отрицательными')

    def test_perimeter_6(self):
        res = perimeter(-6, -8, 10)
        self.assertEqual(res, 'Длины не могут быть отрицательными')

    def test_perimeter_7(self):
        res = perimeter(-131, 1141, 1241411)
        self.assertEqual(res, 'Длины не могут быть отрицательными')

    def test_perimeter_8(self):
        res = perimeter(2210, -4120, 51123)
        self.assertEqual(res, 'Длины не могут быть отрицательными')

    def test_perimeter_9(self):
        res = perimeter(7, 7, -7)
        self.assertEqual(res, 'Длины не могут быть отрицательными')

    def test_perimeter_10(self):
        res = perimeter(3, 4, 8)
        self.assertEqual(res, 'Стороны с такими значениями не могут образовать треугольник')

    def test_perimeter_11(self):
        res = perimeter(-123, -228228228, -676767676767)
        self.assertEqual(res, 'Длины не могут быть отрицательными')

    def test_perimeter_12(self):
        res = perimeter('a', 1, 2)
        self.assertEqual(res, "На вход было подано не число")

    def test_perimeter_13(self):
        res = perimeter(1, 'a', 2)
        self.assertEqual(res, "На вход было подано не число")

    def test_perimeter_14(self):
        res = perimeter(1, 2, 'a')
        self.assertEqual(res, "На вход было подано не число")

    def test_perimeter_15(self):
        res = perimeter('a', 'a', 2)
        self.assertEqual(res, "На вход было подано не число")
        
   

