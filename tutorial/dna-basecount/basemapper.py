#!/usr/bin/python

def mapper(seq):
	freq = dict()
	for x in list(seq):
		if x in freq:
			freq[x] +=1
		else:
			freq[x] = 1
#
	kv = [(x, freq[x]) for x in freq]
	return kv
#
#print mapper("ATCGATCGATAT")	
