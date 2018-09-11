import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()
try:
	cursor.execute("INSERT INTO population VALUES('New York City', \'NY', 840000)")
	cursor.execute("INSERT INTO population VALUES('San Francisco', \'CA', 800000)")

	conn.commit()
except sqlite3.OperationalError:
	print("Oops something went wrong. Try again...")
conn.close()