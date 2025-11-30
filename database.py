import sqlite3
import os

DB_PATH = "flashcards.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS flashcards(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT NOT NULL,
            resposta TEXT NOT NULL,
            nivel INTEGER DEFAULT 1,
            ultima_revisao TEXT,
            proxima_revisao TEXT,
            categoria TEXT
        )
    """)

    conn.commit()
    conn.close()