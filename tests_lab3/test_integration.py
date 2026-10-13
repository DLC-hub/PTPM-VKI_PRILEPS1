import unittest
from unittest.mock import patch
from triangle_calculator import TriangleCalculator
from database import Database
from user_interface import ConsoleUserInterface
from email_service import FakeEmailService
from controller import Controller

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.calculator = TriangleCalculator()
        self.db = Database(":memory:")
        self.ui = ConsoleUserInterface()
        self.email = FakeEmailService()
        self.controller = Controller(self.calculator, self.db, self.ui, self.email)

    def tearDown(self):
        self.db.close()

    @patch('builtins.input', side_effect=['3', '4', '5'])
    def test_new_triangle(self, mock_input):
        with patch.object(self.email, 'send_result') as mock_send:
            result = self.controller.process_triangle()
            self.assertEqual(result, "Тип треугольника: Разносторонний")
            record = self.db.get_record(3, 4, 5)
            self.assertIsNotNone(record)
            self.assertEqual(record[0], "Разносторонний")
            mock_send.assert_called_once_with("Тип треугольника: Разносторонний")

    @patch('builtins.input', side_effect=['3', '4', '5'])
    def test_existing_triangle(self, mock_input):
        self.db.add_record(3, 4, 5, "Разносторонний", None)
        with patch.object(self.email, 'send_result') as mock_send:
            result = self.controller.process_triangle()
            self.assertEqual(result, "Тип треугольника: Разносторонний")
            self.assertEqual(self.db.get_record(3, 4, 5), ("Разносторонний", None))
            mock_send.assert_called_once_with("Тип треугольника: Разносторонний")

    @patch('builtins.input', side_effect=['1', '2', '5'])
    def test_invalid_triangle(self, mock_input):
        with patch.object(self.email, 'send_result') as mock_send:
            result = self.controller.process_triangle()
            self.assertTrue(result.startswith("Ошибка"))
            record = self.db.get_record(1, 2, 5)
            self.assertIsNotNone(record)
            self.assertIsNotNone(record[1])
            mock_send.assert_called_once()

    def test_db_crud(self):
        self.db.add_record(2, 3, 4, "Разносторонний", None)
        self.assertEqual(self.db.get_record(2, 3, 4), ("Разносторонний", None))
        self.db.delete_record(2, 3, 4)
        self.assertIsNone(self.db.get_record(2, 3, 4))

    def test_calc_types(self):
        self.assertEqual(self.calculator.get_triangle_type(3, 3, 3), "Равносторонний")
        self.assertEqual(self.calculator.get_triangle_type(3, 3, 4), "Равнобедренный")
        self.assertEqual(self.calculator.get_triangle_type(3, 4, 5), "Разносторонний")
        self.assertTrue(self.calculator.get_triangle_type(1, 2, 5).startswith("Ошибка"))

if __name__ == '__main__':
    unittest.main()