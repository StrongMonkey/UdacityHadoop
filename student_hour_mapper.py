#!/usr/bin/python

import sys
import time
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None) # skip headers
for line in reader:
	timestring = line[8].split('.')
	hour = time.strptime(timestring[0],"%Y-%m-%d %H:%M:%S").tm_hour
	print "{0}\t{1}".format(line[3],hour)
