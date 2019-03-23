#!/usr/bin/env python3
import geohash2, sqlite3, csv
from difflib import SequenceMatcher


def date_to_days_recip(dat, curr):
	dat_lst = dat.split('-')
	curr_lst = curr.split('-')
	year_days = (int(dat_lst[0])-1900)*365.25-(int(curr_lst[0])-1900)*365.25
	month_days = int(dat_lst[1])*30.25-int(curr_lst[1])*30.25
	days_days = int(dat_lst[2])-int(curr_lst[2])
	return(1/(year_days+month_days+days_days))

def evaluate(inp_str):
	'''The current idea is to compare the geohashed strings to what I already have
	and to use a weighted average based of the ratio the geohashed comparisons
	and also how close the date it to the date of the current date.
	'''
	with open(inp_str, encoding="MAC_ROMAN") as house_data:  # reading in the data from the csv
		my_re = csv.reader(house_data, delimiter=',')
		rows = []
		Rows = []
		err_lst = []
		for row in my_re:
			rows.append(row)

		for row in range(1, len(rows)):
			try:
				Rows.append(
					[
								# float(rows[row][0].split(',')[0].strip()), # lat
								# float(rows[row][0].split(',')[1].strip()), # lon
								(geohash2.encode(float(rows[row][0].split(',')[0].strip()), float(
									rows[row][0].split(',')[1].strip()), precision=100)),  # geohash
								(rows[row][1]),  # address
								(rows[row][2]),  # county
								# date YYYY-MM-DD
								('-'.join(rows[row][3].split('/')[::-1])),
								float(rows[row][4])  # house price
					]
				)
			except ValueError as e:
				err_lst.append(row)

	# making/connecting to the database file
	connec = sqlite3.connect('house_database_geohashed.db')
	c = connec.cursor()  # generating a cursor to the database file

	data = list(c.execute("SELECT geohash, sell_date, price FROM house_data"))

	for i in range(len(data)):
		geohashed_string = data[i][0]
		inp_date = data[i][1]
		weighted_dict1 = {}
		weighted_dict2 = {}

		for e in range(len(data)):
			if (data[e][1] > inp_date) & (data[e][0][:5] == geohashed_string[:5]):
				weighted_dict1[SequenceMatcher(
					None, data[e][0], geohashed_string).ratio()] = data[e][2]
				weighted_dict2[date_to_days_recip(
					data[e][1], inp_date)] = data[e][2]
				# print(weighted_dict2)
		em_dict1 = False
		em_dict2 = False
		if weighted_dict1:
			val1 = int(sum([a*b for a, b in weighted_dict1.items()])) / \
				(len(weighted_dict1) *
					 (sum([a for a, _ in weighted_dict1.items()]))) # Weighted average by proximity.
			em_dict1 = True
		if weighted_dict2:
			val2 = int(sum([a*b for a, b in weighted_dict2.items()])) / \
			(len(weighted_dict2) *
					 (sum([abs(a) for a, _ in weighted_dict2.items()]))) # Weighted average by date.
			em_dict2 = True
			# print(val2,'\n')
		
		a = 3
		b = 20
		if em_dict1 and em_dict2:
			print(val1*a+val2*b)
		elif em_dict1:
			print(val1*a)
		elif em_dict2:
			print(val2*b)
		else:
			print("Empty Dict", "\n")


inp_var =  input("Please give the path to the csv to predict: ")
evaluate(inp_var)
