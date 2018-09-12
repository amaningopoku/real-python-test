import sqlite3
with sqlite3.connect('cars.db') as conn:
	c = conn.cursor()

	c.execute("CREATE TABLE IF NOT EXISTS orders(Make TEXT, Model TEXT, Order_date DATE)")

	orderList = [("Ford", "Expedition", "2016-06-06"),
				("Ford", "Expedition", "2016-07-07"),
				("Ford", "Expedition", "2016-08-08"),
				("Honda", "Civic", "2015-06-08"),
				("Honda", "Civic", "2015-07-09"),
				("Honda", "Civic", "2015-09-10"),
				("Ford", "Explorer", "2017-09-09"),
				("Ford", "Explorer", "2017-09-20"),
				("Ford", "Explorer", "2017-10-10"),
				("Ford", "F-150", "2016-10-10"),
				("Ford", "F-150", "2016-10-04"),
				("Ford", "F-150", "2016-04-10"),
				("Honda", "Accord", "2018-05-19"),
				("Honda", "Accord", "2018-05-20"),
				("Honda", "Accord", "2017-12-12")
				]
	c.executemany("INSERT INTO orders VALUES(?,?,?)", orderList)

	c.execute("SELECT * FROM orders ORDER BY Order_date")
	rows = c.fetchall()
	for r in rows:
		print("Make: " + r[0])
		print("Model: " + r[1])
		print("Order date: " + r[2])
		print("----------------------------------------")