import sys
import random
import csv


with open(sys.argv[1], "w") as out_file_raw:
	out_file = csv.writer(out_file_raw)
	for i in range(0,int(sys.argv[2])):
		row = []
		for j in range(0,int(sys.argv[3])):
			row.append(random.uniform(0,1))
		out_file.writerow(row)
