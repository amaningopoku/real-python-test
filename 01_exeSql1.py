import sqlite3

with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	inventory = [('Ford', 'Expedition', 51000),
					('Ford', 'Explorer', 100000),
					('Ford', 'F-150', 200000),
					('Honda', 'Civic', 60000),
					('Honda', 'Accord', 80000)]

	c.executemany("INSERT INTO inventory VALUES(?,?,?)", inventory)