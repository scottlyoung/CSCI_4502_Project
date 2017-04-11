#!/usr/bin/python 

import matplotlib.pyplot as plt; plt.rcdefaults()
import argparse
import numpy as np
import csv

#TODO: method for bin sorting dates

def grapher(attrNames, attrCounts, attrType):

	y_pos = np.arange(len(tuple(attrNames)))

	plt.barh(y_pos, attrCounts, align='center', alpha=0.5)
	plt.yticks(y_pos, tuple(attrNames))
	plt.xlabel("Number of Occurrences")
	plt.title(attrType + " attribute Frequencies")

	plt.show()
	

def parse(i, fname):

	with open(fname, "r") as inputFile:
		# skip first line
		next(inputFile)
		
		readcsv = csv.reader(inputFile)
		listcsv = list(readcsv)

		names = ['']
		counts = [0]

		for line in listcsv:
			# make sure line is long enough (avoid segfault equivalent)
			if len(line) > i:
				if line[i] in names:
					index = names.index(line[i])
					counts[index] = counts[index] + 1
				else:
					names.append(line[i])
					counts.append(1)
	
	print("Attribute data: ")
	print(names, counts)
	return names, counts
			

def main():
	# argparse?
	# TODO: argparse to choose attribute
	parser = argparse.ArgumentParser(description='Parse data by attribute. Please select one or more data field when executing.')
	parser.add_argument('file', help='filename required')
	parser.add_argument('--product',action='store_const', const=1, help='Product field of data')
	parser.add_argument('--subproduct', action='store_const',const=2, help='subproduct field of data')
	parser.add_argument('--issue', action='store_const',const=3, help='issue field of data')
	parser.add_argument('--subissue', action='store_const',const=4, help='subissue field of data')
	parser.add_argument('--response', action='store_const',const=6, help='response field of data')
	parser.add_argument('--company', action='store_const',const=7, help='company field of data')
	parser.add_argument('--state', action='store_const',const=8, help='state field of data')
	parser.add_argument('--zip', action='store_const',const=9, help='zip code field of data')
	parser.add_argument('--tags', action='store_const',const=10, help='tags field of data')
	parser.add_argument('--consumer', action='store_const',const=11, help='consumder field of data')
	parser.add_argument('--submittedvia', action='store_const',const=12, help='submitted via what medium-field of data')
	parser.add_argument('--status', action='store_const',const=13, help='response status field of data')
	parser.add_argument('--timely', action='store_const',const=14, help='timeliness of response field of data')
	parser.add_argument('--disputed', action='store_const',const=15, help='whether or not the case was disputed field of data')

	args = parser.parse_args()

	# might need this later ;)
	argcounter = 0

	for arg in vars(args):
		if arg == 'file':
			continue
		if getattr(args, arg):
			argcounter +=1
			print("Parsing data for attribute", arg)
			names, counts = parse(getattr(args,arg), args.file)
			print("Graphing data for attribute ", arg)
			grapher(names, counts, arg)

main()
