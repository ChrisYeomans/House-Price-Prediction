#! /usr/bin/env python3
import sqlite3
import csv

def main():
	'''This file creates a database from a csv file.
	This is the first iteration and so does not geohash
	any of the locations.
	'''
	with open('HouseData.csv', encoding='MAC_ROMAN') as house_data: # reading in the data from the csv
		my_re = csv.reader(house_data, delimiter=',')
		rows = []
		Rows = []
		err_lst = []
		for row in my_re:
			rows.append(row)

	for i in range(len(rows)):
		try:
			print(rows[i])
		except UnicodeDecodeError as e:
			sys.stderr.write(str(i)+'\n')
	connec = sqlite3.connect('house_database.db') # making/connecting to the database file
	c = connec.cursor() # generating a cursor to the database file

	# making the table
	c.execute("CREATE TABLE house_data (ID INTEGER PRIMARY KEY, address text, county text, lat real, long real, sell_date date, price real)")

	cntr = 0
	for j in Rows: # Insert items into the table
		c.execute("INSERT INTO 	house_data(address, county, lat, long, sell_date, price) VALUES (?, ?, ?, ?, ?, ?)", (j[2], j[3], j[0], j[1], j[4], j[5])) # filling up the table
		cntr+=1
		if cntr == 10000: # using a cntr system to make commits to the database file to keep it in manageable chunks but keep speed
			connec.commit()
			cntr = 0
	connec.commit()
	connec.close()

if __name__ == "__main__":
	main()