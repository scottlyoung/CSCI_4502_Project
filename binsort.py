#!/usr/bin/python

import numpy as np
import matplotlib

def parse():
	f = open("Consumer_Complaints.csv", "r")
	# first line does not contain relevant data
	firstLine = f.readline()

	for line in f:
		# comma delimited
		lineList = line.split(",")
		# TODO: strip newline characters and quotes
		# lineList contains array  of all comma delimited attributes

def main():
	# argparse?
	parse()

main()
