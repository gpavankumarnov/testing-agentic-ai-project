import sqlite3
from typing import List, Dict, Optional


class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        # BUG3: Connection not established before using it
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row
        return self.connection

    def create_users_table(self):
        """
        Issue: When self.connection is None (not established),
        calling .cursor() on None raises AttributeError
        """
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )
        self.connection.commit()

    def insert_user(self, username: str, email: str) -> int:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, email) VALUES (?, ?)", (username, email)
        )
        self.connection.commit()
        return cursor.lastrowid

    def get_user_by_id(self, user_id: int) -> Optional[Dict]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()

        if row:
            return dict(row)
        return None

    def get_all_users(self) -> List[Dict]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        return [dict(row) for row in rows]

    def update_user_email(self, user_id: int, new_email: str):
        cursor = self.connection.cursor()
        cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
        self.connection.commit()

    def delete_user(self, user_id: int) -> bool:
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.connection.commit()

        return cursor.rowcount > 0

    def close(self):
        if self.connection:
            self.connection.close()
