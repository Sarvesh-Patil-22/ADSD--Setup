import sqlite3

def create_sqlite_database(tutorial):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(tutorial)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

res = cur.execute("SELECT score FROM movie")
res.fetchall()

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit() 

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

try :
    cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")


con.close()
con.close()