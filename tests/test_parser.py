import unittest
import os
from unittest.mock import patch, MagicMock
from src.parser import ForumParser
from src.database import DatabaseRepository


class TestForumParser(unittest.TestCase):
    def setUp(self):
        self.parser = ForumParser()
        self.db = DatabaseRepository(':memory:')

        # Читаем файл
        path = os.path.join(os.path.dirname(__file__), "sample_forum.html")
        with open(path, "r", encoding="utf-8") as f:
            self.html = f.read()

    def tearDown(self):
        self.db.close()

    @patch('src.parser.requests.get')
    def test_parse(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.text = self.html
        mock_get.return_value = mock_resp

        data = self.parser.parse_page("http://test.com")

        # Проверяем, что нашли 2 поста
        self.assertEqual(len(data), 2)

        # Проверяем первый пост
        self.assertEqual(data[0]["id"], 1)
        self.assertEqual(data[0]["name"], "Ivan")
        self.assertIn("<b>мир</b>", data[0]["message"])

    def test_save(self):
        data = [{"id": 10, "name": "Test", "message": "Text"}]
        self.parser.save_to_db(data, self.db)

        record = self.db.get_by_id(10)
        self.assertIsNotNone(record)
        self.assertEqual(record["name"], "Test")


if __name__ == '__main__':
    unittest.main()