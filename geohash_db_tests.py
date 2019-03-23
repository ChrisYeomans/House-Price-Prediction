#! /usr/bin/env python3
import sqlite3, sys
from difflib import SequenceMatcher

def main():
	'''This file tests the geohashed database'''
	connec = sqlite3.connect('house_database_geohashed.db') # making/connecting to the database file
	c = connec.cursor() # generating a cursor to the database file


	first_500 = list(c.execute("SELECT * FROM house_data LIMIT 500"))
	all_arr = list(c.execute("SELECT * FROM house_data"))


	for item in range(500):
		print(first_500[item])
		for dat in all_arr:
			if dat != first_500[item]:
				if first_500[item][2][:4] == dat[2][:4]:
					print(dat)

	for item in range(500):
		curr_ratio = 0
		min_tuple = ()
		for dat in all_arr:
			if dat != first_500[item]:
				''' Abandoned in favour of a different approach
				#print geohash2.decode_exactly(first_500[item][2])[:2]
				#print geohash2.decode_exactly(dat[2])[:2]
				#print item			
				dist = haversine((float(e) for e in geohash2.decode_exactly(first_500[item][2])[:2]), (float(e) for e in geohash2.decode_exactly(dat[2])[:2]))
				#print dist
				#print curr_min
				if dist < curr_min:
					curr_min = dist
					min_tuple = dat
					#print "\n"
					if curr_min == 0:
						sys.stderr.write("rip\n")				
						break
				'''			
				ratio = SequenceMatcher(None, first_500[item][2], dat[2]).ratio()
				if ratio > curr_ratio:
					curr_ratio = ratio
					min_tuple = dat
					if ratio == 1:
						break

		print(first_500[item])
		print(min_tuple)
		print("\n")

if __name__ = "__main__":
	main()