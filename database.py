import sqlite3

class Database:
    def __init__(self, db_name="triangles.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS triangles (
                a REAL, b REAL, c REAL,
                type TEXT, error TEXT,
                PRIMARY KEY (a, b, c)
            )
        """)
        self.conn.commit()

    def add_record(self, a, b, c, triangle_type, error):
        self.cursor.execute(
            "INSERT OR REPLACE INTO triangles VALUES (?, ?, ?, ?, ?)",
            (a, b, c, triangle_type, error)
        )
        self.conn.commit()

    def get_record(self, a, b, c):
        self.cursor.execute(
            "SELECT type, error FROM triangles WHERE a=? AND b=? AND c=?",
            (a, b, c)
        )
        return self.cursor.fetchone()

    def delete_record(self, a, b, c):
        self.cursor.execute(
            "DELETE FROM triangles WHERE a=? AND b=? AND c=?",
            (a, b, c)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()