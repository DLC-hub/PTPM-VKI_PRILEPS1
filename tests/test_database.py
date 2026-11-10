import unittest
from src.database import DatabaseRepository
from src.exceptions import ValidationError, RecordNotFoundError, DuplicateRecordError

class TestDatabaseRepository(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseRepository(':memory:')
        self.db.add(1, "Alice", "Hello")
        self.db.add(2, "Bob", "Hi")

    def tearDown(self):
        self.db.close()

    def test_add_ok(self):
        self.assertTrue(self.db.add(3, "Charlie", "New"))
        self.assertEqual(self.db.get_by_id(3)["name"], "Charlie")

    def test_add_dup(self):
        with self.assertRaises(DuplicateRecordError):
            self.db.add(1, "Alice", "Hello")

    def test_get_id(self):
        self.assertEqual(self.db.get_by_id(1)["name"], "Alice")
        self.assertIsNone(self.db.get_by_id(99))

    def test_get_name(self):
        self.assertEqual(len(self.db.get_by_name("Alice")), 1)
        self.assertEqual(len(self.db.get_by_name("Nobody")), 0)

    def test_update(self):
        self.assertTrue(self.db.update(1, "New text"))
        self.assertEqual(self.db.get_by_id(1)["message"], "New text")

    def test_update_error(self):
        with self.assertRaises(RecordNotFoundError):
            self.db.update(99, "New text")

    def test_delete(self):
        self.assertTrue(self.db.delete(2))
        self.assertIsNone(self.db.get_by_id(2))

    def test_delete_error(self):
        with self.assertRaises(RecordNotFoundError):
            self.db.delete(99)

if __name__ == '__main__':
    unittest.main()