import unittest
from rectangle import area, perimeter

class RectangleTestArea(unittest.TestCase):
    def test_area_1(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_area_2(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_3(self):
        res = area(1, 100)
        self.assertEqual(res, 100)

    def test_area_4(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_area_5(self):
        res = area(1000, 2488)
        self.assertEqual(res, 2488000)

    def test_area_6(self):
        res = area(2.5, 4.0)
        self.assertAlmostEqual(res, 10.0)

    def test_area_7(self):
        res = area(1.5, 2.5)
        self.assertAlmostEqual(res, 3.75)

    def test_area_8(self):
        res = area(0, 101231231)
        self.assertEqual(res, 0)

    def test_area_9(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_area_10(self):
        res = area(-5, 112312312144444)
        self.assertEqual(res, 'Длины сторон прямоугольника не могут быть отрицательными')
        

    def test_area_11(self):
        res = area(-3564892, -4743657364958763)
        self.assertEqual(res, 'Длины сторон прямоугольника не могут быть отрицательными')

    def test_area_12(self):
        res = area(0.1, 0.2)
        self.assertAlmostEqual(res, 0.02)

    def test_area_13(self):
        self.assertEqual(area(345, 84), area(84, 345))

    def test_area_14(self):
        res = area('a', -23)
        self.assertEqual(res, 'На вход было подано не число')

    def test_area_15(self):
        res = area('a', 'b')
        self.assertEqual(res, 'На вход было подано не число')

    def teast_area_16(self):
        res = area(123, 'a')
        self.assertEqual(res, 'На вход было подано не число')
    



class RectangleTestPerimeter(unittest.TestCase):
    def test_perimetr_1(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_2(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_3(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)

    def test_perimeter_3(self):
        res = perimeter(7, 7)
        self.assertEqual(res, 28)

    def test_perimeter_4(self):
        res = perimeter(1, 100)
        self.assertEqual(res, 202)

    def test_perimeter_5(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)

    def test_perimeter_6(self):
        res = perimeter(123, 23432)
        self.assertEqual(res, 47110)

    def test_perimeter_7(self):
        res = perimeter(2.5, 4.67)
        self.assertAlmostEqual(res, 14.34)

    def test_perimeter_8(self):
        res = perimeter(1.5, 2.5)
        self.assertAlmostEqual(res, 8.0)

    def test_perimeter_10(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_11(self):
        res = perimeter(67, 52)
        self.assertEqual(res, 238)

    def test_perimeter_12(self):
        res = perimeter(148, 228)
        self.assertEqual(res, 752)

    def test_perimeter_13(self):
        res = perimeter(0.1, 0.2)
        self.assertAlmostEqual(res, 0.6)

    def test_perimeter_14(self):
        self.assertEqual(perimeter(3, 8), perimeter(8, 3))

    def test_perimeter_15(self):
        res = perimeter(-1, 0)
        self.assertEqual(res, 'Длины сторон прямоугольника не могут быть отрицательными')

    def test_perimeter_16(self):
        res = perimeter(-123123, 123123123123123)
        self.assertEqual(res, 'Длины сторон прямоугольника не могут быть отрицательными')

    def test_perimeter_17(self):
        res = perimeter(-12, -23)
        self.assertEqual(res, 'Длины сторон прямоугольника не могут быть отрицательными')

    def test_perimeter_18(self):
        res = perimeter('a', -23)
        self.assertEqual(res, 'На вход было подано не число')

    def test_perimeter_19(self):
        res = perimeter('a', 'b')
        self.assertEqual(res, 'На вход было подано не число')

    def test_perimeter_18(self):
        res = perimeter(123, 'a')
        self.assertEqual(res, 'На вход было подано не число')


