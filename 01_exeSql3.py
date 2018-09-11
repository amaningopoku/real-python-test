import sqlite3

with sqlite3.connect("cars.db") as conn:
	c=conn.cursor()
	c.execute("SELECT Make, Model, Quantity FROM inventory WHERE Make = 'Ford'")

	print("\nFORD CARS\n")
	rows = c.fetchall()

	for r in rows:
		print(r[0], r[1])