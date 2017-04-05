#!/usr/bin/python

import sys
import csv

with open(sys.argv[1], "r") as inputFile:
	next(inputFile)
	
	readcsv = csv.reader(inputFile)
	listcsv = list(readcsv)
	stateDict = {}
	for g in listcsv:
		cityState = g[8]
		state = cityState[-2:]
		if(stateDict.has_key(state)):
			stateDict[state] = (stateDict[state]+1)
		else:
			stateDict.update({state: 1})
	
	print(str(stateDict))
