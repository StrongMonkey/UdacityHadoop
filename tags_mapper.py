#! /usr/bin/python

import csv
import sys

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None) # skip headers
for line in reader:
	tags = line[2].split(' ')
	for tag in tags:
		if len(tag) != 0:
			print tag
