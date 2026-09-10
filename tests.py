import unittest
from main import compute_triangle


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):

        t_type, coords = compute_triangle("5", "5", "5")
        self.assertEqual(t_type, "равносторонний")
        self.assertEqual(len(coords), 3)

    def test_isosceles(self):

        t_type, coords = compute_triangle("5", "5", "6")
        self.assertEqual(t_type, "равнобедренный")

