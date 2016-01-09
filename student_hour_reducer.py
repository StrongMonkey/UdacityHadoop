#!/usr/bin/python

import sys

oldKey = None
hourCount = []
for i in range(24):
        hourCount.append(0)
for line in sys.stdin:
	data = line.strip().split("\t")
	thisKey = data[0]
	hour = int(data[1])
	if oldKey and thisKey != oldKey:
		m = max(hourCount)
		for i in range(24):
			if hourCount[i] == m:
				print "{0}\t{1}".format(oldKey,i)
		hourCount = []
		for i in range(24):
        		hourCount.append(0)
	oldKey = thisKey
	hourCount[hour] = hourCount[hour] + 1
if oldKey != None:
	m = max(hourCount)
        for i in range(24):
        	if hourCount[i] == m:
                	print "{0}\t{1}".format(oldKey,i)

	 	
