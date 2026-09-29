import unittest
from main import compute_triangle


class TestMyProject(unittest.TestCase):

    def test_equilateral(self):
        """ треугольник"""
        t_type, coords = compute_triangle("5", "5", "5")
        self.assertEqual(t_type, "равносторонний")
        self.assertEqual(len(coords), 3)

    def test_isosceles_ab(self):
        """(A=B)"""
        t_type, _ = compute_triangle("5", "5", "6")
        self.assertEqual(t_type, "равнобедренный")

    def test_isosceles_ac(self):
        """ (A=C)"""
        t_type, _ = compute_triangle("5", "6", "5")
        self.assertEqual(t_type, "равнобедренный")

    def test_isosceles_bc(self):
        """(B=C)"""
        t_type, _ = compute_triangle("6", "5", "5")
        self.assertEqual(t_type, "равнобедренный")

    def test_scalene(self):

        t_type, _ = compute_triangle("3", "4", "5")
        self.assertEqual(t_type, "разносторонний")

    def test_not_triangle_inequality(self):
        """Тут я делал нарушение неравенства, не треугольник """
        t_type, coords = compute_triangle("1", "1", "3")
        self.assertEqual(t_type, "не треугольник")
        self.assertEqual(coords, [(-1, -1), (-1, -1), (-1, -1)])

    def test_not_triangle_degenerate(self):
        """Вырожденный треугольник"""
        t_type, _ = compute_triangle("1", "2", "3")
        self.assertEqual(t_type, "не треугольник")

    def test_negative_side(self):
        """Отрицательная сторона"""
        t_type, _ = compute_triangle("-3", "4", "5")
        self.assertEqual(t_type, "не треугольник")

    def test_zero_side(self):
        """Нулевая сторона"""
        t_type, _ = compute_triangle("0", "4", "5")
        self.assertEqual(t_type, "не треугольник")

    def test_non_numeric(self):
        """Нечисловые данные"""
        t_type, coords = compute_triangle("abc", "4", "5")
        self.assertEqual(t_type, "")
        self.assertEqual(coords, [(-2, -2), (-2, -2), (-2, -2)])

    def test_float_sides(self):
        """Стороны с плавающей точкой"""
        t_type, _ = compute_triangle("3.5", "4.5", "5.5")
        self.assertEqual(t_type, "разносторонний")

    def test_tiny_sides(self):
        """Очень маленькие стороны"""
        t_type, _ = compute_triangle("0.1", "0.1", "0.1")
        self.assertEqual(t_type, "равносторонний")

    def test_huge_sides(self):
        """Тут получаются очень большие стороны, ну вроде"""
        t_type, _ = compute_triangle("10000", "10000", "10000")
        self.assertEqual(t_type, "равносторонний")

    def test_almost_equilateral(self):
        """Почти равносторонний"""
        t_type, _ = compute_triangle("5.000000001", "5", "5")
        self.assertEqual(t_type, "равносторонний")

    def test_empty_string(self):
        """Пустая строка"""
        t_type, coords = compute_triangle("", "4", "5")
        self.assertEqual(t_type, "")
        self.assertEqual(coords, [(-2, -2), (-2, -2), (-2, -2)])

    def test_none_input(self):
        """None вместо числа"""
        t_type, coords = compute_triangle(None, "4", "5")
        self.assertEqual(t_type, "")
        self.assertEqual(coords, [(-2, -2), (-2, -2), (-2, -2)])

    def test_coords_boundaries(self):

        _, coords = compute_triangle("3", "4", "5")
        for x, y in coords:
            self.assertTrue(0 <= x <= 100)
            self.assertTrue(0 <= y <= 100)

    def test_coords_y_axis_flip(self):
        """Тута проверка инверсии оси Y """
        _, coords = compute_triangle("3", "4", "5")

        c_y = coords[2][1]
        a_y = coords[0][1]
        self.assertLess(c_y, a_y)  # Y вроде инвертирован

    def test_return_type(self):

        result = compute_triangle("3", "4", "5")
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)

    def test_all_invalid_numeric(self):

        t_type, _ = compute_triangle("a", "b", "c")
        self.assertEqual(t_type, "")

    def test_one_invalid_numeric(self):

        t_type, _ = compute_triangle("3", "abc", "5")
        self.assertEqual(t_type, "")


if __name__ == '__main__':
    unittest.main()