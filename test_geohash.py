#! usr/bin/python2

import geohash2
from haversine import haversine

my_string = "ebcdefghebcdefgh"
error_margins = [0]*len(my_string)
lat_long = [0]*len(my_string)

for i in xrange(len(my_string)):
	error_margins[i] = geohash2.decode_exactly(my_string[:i])[2:4]
	lat_long[i] = geohash2.decode_exactly(my_string[:i])[:2]

for i in lat_long:
	print haversine((0.0, 0.0), i)





