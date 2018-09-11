import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()
cursor.execute("INSERT INTO populations VALUES('New York City', \'NY', 840000)")
cursor.execute("INSERT INTO populations VALUES('San Francisco', \'CA', 800000)")

conn.commit()
conn.close()