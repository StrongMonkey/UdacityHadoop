#! /usr/bin/python

import sys

oldKey = None
list = []
for line in sys.stdin:
	data = line.strip().split("\t")	
	thisKey = data[0]
	if oldKey and oldKey != thisKey:
		print oldKey, "\t" , list[0:len(list)]  
		del list[:]
	oldKey = thisKey
	list.append(data[1])
if oldKey != None:
	print oldKey, "\t", list[0:len(list)]

