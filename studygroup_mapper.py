#! /usr/bin/python

import csv 
import sys

reader = csv.reader(sys.stdin,delimiter='\t')
next(reader,None)
for line in reader:
	if line[5] == "question":
		print "{0}\t{1}".format(line[0],line[3])
	else:
		print "{0}\t{1}".format(line[6],line[3])
