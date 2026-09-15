import unittest
from main import compute_triangle


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        """Равносторонний треугольник"""
        t_type, coords = compute_triangle("5", "5", "5")
        self.assertEqual(t_type, "равносторонний")
        self.assertEqual(len(coords), 3)

    def test_isosceles(self):
        """Равнобедренный треугольник"""
        t_type, coords = compute_triangle("5", "5", "6")
        self.assertEqual(t_type, "равнобедренный")

    def test_scalene(self):
        """Разносторонний треугольник"""
        t_type, coords = compute_triangle("3", "4", "5")
        self.assertEqual(t_type, "разносторонний")

    def test_not_a_triangle(self):
        """Не треугольник (нарушено неравенство)"""
        t_type, coords = compute_triangle("1", "1", "3")
        self.assertEqual(t_type, "не треугольник")
        self.assertEqual(coords, [(-1, -1), (-1, -1), (-1, -1)])

    def test_invalid_numeric(self):
        """Отрицательные числа и нули"""
        t_type, coords = compute_triangle("-3", "4", "5")
        self.assertEqual(t_type, "не треугольник")
        self.assertEqual(coords, [(-1, -1), (-1, -1), (-1, -1)])

    def test_non_numeric(self):
        """Нечисловые данные"""
        t_type, coords = compute_triangle("abc", "4", "5")
        self.assertEqual(t_type, "")
        self.assertEqual(coords, [(-2, -2), (-2, -2), (-2, -2)])


if __name__ == '__main__':
    unittest.main()

