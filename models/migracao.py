import sqlite3

conn = sqlite3.connect("flashcards.db")
cur = conn.cursor()

cur.execute("ALTER TABLE flashcards ADD COLUMN categoria TEXT;")

conn.commit()
conn.close()

print("Coluna categoria adicionada!")