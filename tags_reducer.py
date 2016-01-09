#! /usr/bin/python

import sys

oldKey = None
count = 0
list = []
for line in sys.stdin:
	thisKey = line.strip()
	if oldKey and thisKey != oldKey :
		list.append((oldKey,count))
		count = 0
	oldKey = thisKey
	count = count + 1
list.sort(key=lambda tup: tup[1], reverse=True)
for x in range(0,10):
	if x < len(list):
		print list[x]
		
