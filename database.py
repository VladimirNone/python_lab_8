import sqlite3

DB_NAME = "glossary.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS terms (
            keyword TEXT PRIMARY KEY,
            description TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_term(keyword, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO terms (keyword, description) VALUES (?, ?)", (keyword, description))
        conn.commit()
        return True, "Term added successfully."
    except sqlite3.IntegrityError:
        return False, "Term already exists."
    finally:
        conn.close()

def update_term(keyword, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE terms SET description = ? WHERE keyword = ?", (description, keyword))
    conn.commit()
    conn.close()

def delete_term(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM terms WHERE keyword = ?", (keyword,))
    conn.commit()
    conn.close()

def get_term(keyword):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT keyword, description FROM terms WHERE keyword = ?", (keyword,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"keyword": row[0], "description": row[1]}
    return None

def list_terms():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT keyword, description FROM terms")
    rows = cursor.fetchall()
    conn.close()
    return [{"keyword": row[0], "description": row[1]} for row in rows]

init_db()
