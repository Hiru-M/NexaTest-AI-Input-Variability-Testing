import sqlite3
from datetime import datetime
from src.input_handler import InputHandler

class SQLiteStore:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY,
            prompt TEXT,
            similarity REAL,
            created_at TEXT
        )
        """)
        self.conn.commit()

    def save_run(self, prompt: str, similarity: float):
        self.conn.execute(
            "INSERT INTO runs (prompt, similarity, created_at) VALUES (?, ?, ?)",
            (prompt, similarity, datetime.utcnow().isoformat())
        )
        self.conn.commit()
    def get_recent_runs(self, limit: int = 5):
        cursor = self.conn.execute(
            """
            SELECT id, prompt, similarity, created_at
            FROM runs
            ORDER BY created_at DESC
            LIMIT ?
            """,
            (limit,)
        )
        rows = cursor.fetchall()
        return [
        {
            "id": row[0],
            "prompt": row[1],
            "similarity": row[2],
            "created_at": row[3],
        }
        for row in rows
    ]
