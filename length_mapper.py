#! /usr/bin/python

import sys
import csv
reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None) # skip headers
for line in reader:
	data = line
	if len(data) == 19:
		if data[5] == "question":
			print "{0}\t{1}\t{2}".format(data[0],0,len(data[4]))
		elif data[5] == "answer":
			print "{0}\t{1}\t{2}".format(data[6],1,len(data[4]))	
