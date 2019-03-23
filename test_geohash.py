#! usr/bin/env python2
import geohash2
from haversine import haversine

def main():
	'''This is just a few experiments
	on geohashing using the geohash2 library
	and the haversine library.
	'''
	my_string = "ebcdefghebcdefgh"
	error_margins = [0]*len(my_string)
	lat_long = [0]*len(my_string)

	for i in xrange(len(my_string)):
		error_margins[i] = geohash2.decode_exactly(my_string[:i])[2:4]
		lat_long[i] = geohash2.decode_exactly(my_string[:i])[:2]

	for i in lat_long:
		print haversine((0.0, 0.0), i)

if __name__ == "__main__":
	main()