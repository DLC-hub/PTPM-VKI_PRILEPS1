import sqlite3
from src.exceptions import ValidationError, RecordNotFoundError, DuplicateRecordError


class DatabaseRepository:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._init_db()

    def _init_db(self):
        self.cursor.execute('''
            create table if not exists comments (
                id integer primary key,
                name text not null,
                message text not null
            )
        ''')
        self.conn.commit()

    def _validate_input(self, comment_id, username, message):
        if not isinstance(comment_id, int):
            raise ValidationError("comment_id должен быть int")
        if not isinstance(username, str) or len(username) == 0 or len(username) > 256:
            raise ValidationError("name: строка от 1 до 256")
        if not isinstance(message, str) or len(message) == 0 or len(message) > 8096:
            raise ValidationError("message: строка от 1 до 8096")

    def get_by_id(self, comment_id):
        self.cursor.execute("select * from comments where id = ?", (comment_id,))
        row = self.cursor.fetchone()
        if row:
            return {"id": row[0], "name": row[1], "message": row[2]}
        return None

    def get_by_name(self, username):
        self.cursor.execute("select * from comments where name = ?", (username,))
        rows = self.cursor.fetchall()
        return [{"id": r[0], "name": r[1], "message": r[2]} for r in rows]

    def add(self, comment_id, username, message):
        self._validate_input(comment_id, username, message)
        try:
            self.cursor.execute("insert into comments (id, name, message) values (?, ?, ?)",
                                (comment_id, username, message))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            raise DuplicateRecordError("Запись с таким ID уже есть")

    def update(self, comment_id, new_message):
        if not isinstance(new_message, str) or len(new_message) == 0 or len(new_message) > 8096:
            raise ValidationError("new_message: строка от 1 до 8096")

        self.cursor.execute("update comments set message = ? where id = ?", (new_message, comment_id))
        if self.cursor.rowcount == 0:
            raise RecordNotFoundError("Запись не найдена")
        self.conn.commit()
        return True

    def delete(self, comment_id):
        self.cursor.execute("delete from comments where id = ?", (comment_id,))
        if self.cursor.rowcount == 0:
            raise RecordNotFoundError("Запись не найдена")
        self.conn.commit()
        return True

    def close(self):
        self.conn.close()