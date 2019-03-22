#! /usr/bin/python
import sqlite3

connec = sqlite3.connect('house_database.db')
c = connec.cursor()

for item in c.execute("SELECT * FROM house_data WHERE sell_date > '2017-09-10' AND sell_date < '2017-10-10'"): # test 1
	print(item)

for item in c.execute("SELECT * FROM house_data WHERE price >= 200000 AND price <= 277000"): # test 2
	print(item)

for item in c.execute("SELECT * FROM house_data WHERE price > 1000000 LIMIT 1"): # test 3
	print(item)

c.execute("SELECT AVG(price) FROM house_data WHERE sell_date >= '2018-01-01' AND sell_date <= '2018-01-31'") # test 4
print(str(c.fetchone()).replace('(', ' ').replace(')', ' ').replace(',', ' ').strip())

for item in c.execute("SELECT sell_date, price FROM house_data WHERE sell_date >= '2016-06-01' AND sell_date <= '2016-06-30' ORDER BY price DESC"): # test 5
	print(item)

c.execute("SELECT COUNT(price) FROM house_data WHERE price > 400000") # test 6
print(str(c.fetchone()).replace('(', ' ').replace(')', ' ').replace(',', ' ').strip())

c.execute("SELECT AVG(price) FROM house_data WHERE sell_date >= '2018-02-01' AND sell_date <= '2018-02-28'") # test 7
feb18_avg = (float(str(c.fetchone()).replace('(', ' ').replace(')', ' ').replace(',', ' ').strip()))
c.execute("SELECT AVG(price) FROM house_data WHERE sell_date >= '2018-03-01' AND sell_date <= '2018-03-31'")
march18_avg = (float(str(c.fetchone()).replace('(', ' ').replace(')', ' ').replace(',', ' ').strip()))
print(((march18_avg-feb18_avg)*100)/feb18_avg)

c.execute("SELECT AVG(price) FROM house_data WHERE sell_date >= '2015-01-01' AND sell_date <= '2015-12-31'") # test 8
y15_avg = (float(str(c.fetchone()).replace('(', ' ').replace(')', ' ').replace(',', ' ').strip()))
c.execute("SELECT AVG(price) FROM house_data WHERE sell_date >= '2016-01-01' AND sell_date <= '2016-12-31'")
y16_avg = (float(str(c.fetchone()).replace('(', ' ').replace(')', ' ').replace(',', ' ').strip()))
print(((y15_avg-y16_avg)*100)/y15_avg)


connec.close()