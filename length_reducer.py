#! /usr/bin/python

import sys

oldKey = None
count = 0
post_length = 0
total_length = 0
for line in sys.stdin:
	data = line.strip().split("\t")
	thisKey = data[0]
	if oldKey and oldKey != thisKey:
		if count == 0:
			print "{0}\t{1}\t{2}".format(oldKey,post_length,0)
		else:
			print "{0}\t{1}\t{2}".format(oldKey,post_length,total_length/count)
		post_length = 0
		count = 0
		total_length = 0
	oldKey = thisKey
	if int(data[1]) == 0:
		post_length = int(data[2])
	else:
		total_length = total_length + int(data[2])
		count = count + 1
if oldKey != None:
	if count == 0:
          	print "{0}\t{1}\t{2}".format(oldKey,post_length,0)   
        else:
                print "{0}\t{1}\t{2}".format(oldKey,post_length,total_length/count) 	
