import sqlite3

def create_sqlite_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS example (id INTEGER PRIMARY KEY, date TEXT, todo TEXT)")
    cursor.execute("INSERT INTO example VALUES (1, '2024/09/21', 'Hello World')")
    cursor.execute("INSERT INTO example VALUES (2, '2024/09/21', 'こんにちは世界')")
    cursor.execute("INSERT INTO example VALUES (3, '2024/09/21', 'Bonjour le monde')")
    conn.commit()
    cursor.execute("SELECT * FROM example")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

if __name__ == '__main__':
    create_sqlite_database("example.db")
