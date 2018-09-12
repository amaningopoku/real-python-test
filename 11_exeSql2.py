import sqlite3
with sqlite3.connect("cars.db") as conn:
	c = conn.cursor()
	c.execute("SELECT inventory.make, inventory.model, inventory.quantity, orders.Order_date FROM inventory INNER JOIN orders ON inventory.model = orders.model")
	rows = c.fetchall()
	for r in rows:
		print("----------------------------------------")
		print("Make and Model: " + r[0], r[1])
		print("Quantity: " + str(r[2]))
		print("Order date: " + r[3])
		print("----------------------------------------")