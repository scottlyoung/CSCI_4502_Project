#!/usr/bin/python

import sys
import random
import csv

'''
this program will create a smaller cav from a random sample of entries of a larger one.
Run with <your python interpreter> randSampCreat.py <input file> <output file> <number of entries to put in the output file>
'''

with open(sys.argv[1], "r") as in_file_raw:
	with open(sys.argv[2], "w") as out_file_raw:
		in_file = csv.reader(in_file_raw)
		out_file = csv.writer(out_file_raw)
		num_entries_input = sum(1 for line in in_file)
		num_entries_output = int(sys.argv[3])
		if num_entries_input <= num_entries_output:
			raise ValueError("More output entries then input entries")
		entries = random.sample(range(2, num_entries_input), num_entries_output)
		entries.append(1)
		in_file_raw.seek(0)
		line_num = 0
		for line in in_file:
			line_num = line_num + 1
			if line_num in entries:
				out_file.writerow(line)
