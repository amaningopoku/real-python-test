import sqlite3
with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()

	c.execute("UPDATE inventory SET Quantity=120000 WHERE Model='Explorer'")
	c.execute("UPDATE inventory SET Quantity=500000 WHERE Model='Civic'")

	print("\nUPDATED LIST\n")

	c.execute("SELECT Make, Model, Quantity FROM inventory")

	rows = c.fetchall()
	for r in rows:
		print(r[0], r[1], r[2])