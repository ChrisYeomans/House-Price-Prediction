#! /usr/bin/python
import sqlite3
import csv

with open('HouseData.csv', encoding='MAC_ROMAN') as house_data: # reading in the data from the csv
	my_re = csv.reader(house_data, delimiter=',')
	rows = []
	Rows = []
	err_lst = []
	for row in my_re:
		rows.append(row)
	'''
	for i in range(10):
		print(rows[i])
	'''
	for row in range(1, len(rows)):
		try:
			Rows.append(
				[
					float(rows[row][0].split(',')[0].strip()), # lat
					float(rows[row][0].split(',')[1].strip()), # lon
					rows[row][1], # address
					rows[row][2],# county
					'-'.join(rows[row][3].split('/')[::-1]), # date YYYY-MM-DD
					float(rows[row][4]) # house price
				]
			)
		except ValueError as e:
			err_lst.append(row)

#print(err_lst)
'''
for i in range(len(rows)):
	try:
		print(rows[i])
	except UnicodeDecodeError as e:
		print(i)
'''

connec = sqlite3.connect('house_database.db') # making/connecting to the database file
c = connec.cursor() # generating a cursor to the database file

# making the table
c.execute("CREATE TABLE house_data (ID INTEGER PRIMARY KEY, address text, county text, lat real, long real, sell_date date, price real)")
'''
c.execute("CREATE TABLE house_location (address text, county text, lat real, lon real)") # making location and data tables
c.execute("CREATE TABLE house_data (address text, sell_date date, price real)")
'''
cntr = 0
for j in Rows:
	c.execute("INSERT INTO 	house_data(address, county, lat, long, sell_date, price) VALUES (?, ?, ?, ?, ?, ?)", (j[2], j[3], j[0], j[1], j[4], j[5])) # filling up the table
	cntr+=1
	if cntr == 10000: # using a cntr system to make commits to the database file to keep it in manageable chunks but keep speed
		connec.commit()
		cntr = 0

'''
for item in c.execute("SELECT * FROM house_data WHERE sell_date > '2017-09-10' AND sell_date < '2017-10-10'"):
	print(item)
'''

connec.commit()
connec.close()