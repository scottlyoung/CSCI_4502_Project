#!/usr/bin/python

import numpy as np
import matplotlib
import argparse

def parse():
	f = open("complaintNarratives.csv", "r")
	# first line does not contain relevant data
	firstLine = f.readline()
	
	i = 1
	names = ['']
	counts = [0]

	for line in f:
		# comma delimited
		lineList = line.split(",")
		# check for last line
		if lineList[0] == '\n':
			continue
		if len(lineList) > i:
			if lineList[i] in names:
				index = names.index(lineList[i])
				counts[index] = counts[index] + 1
			else:
				names.append(lineList[i])
				counts.append(1)
	
	print(names, counts)
	return names, counts
			

def main():
	# argparse?
	# TODO: argparse to choose attribute
	parser = argparse.ArgumentParser(description='Parse data by attribute.')
	parser.add_argument('file', nargs='+', help='filename required')
	names, counts = parse()

main()
