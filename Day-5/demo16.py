
import sqlite3

conn = sqlite3.connect(r"C:\\Users\\Namandeep\\Downloads\\Python\\Day5\\prod.db")
sth = conn.cursor()

sth.execute("""
CREATE TABLE IF NOT EXISTS prod (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
""")

sth.execute("INSERT INTO prod (name, price) VALUES (?, ?)", ("Laptop", 70000))

conn.commit()

sth.execute("SELECT * FROM prod")

for var in sth:
    print(var)

conn.close()