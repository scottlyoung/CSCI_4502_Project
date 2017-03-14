import sys
import csv

with open(sys.argv[1], "r") as in_file_raw:
	in_file = csv.reader(in_file_raw)
	complaints = {}
	for line in in_file:
		next(in_file, None)
		if not line[7] in complaints:
			complaints[line[7]] = {}
		if not line[3] in complaints[line[7]]:
			complaints[line[7]][line[3]] = {}
		if line[4] in complaints[line[7]][line[3]]:
			complaints[line[7]][line[3]][line[4]] += 1
		else:
			complaints[line[7]][line[3]][line[4]] = 1
	for company in complaints:
		total = 0
		for issue in complaints[company]:
			for subIssue in complaints[company][issue]:
				total += complaints[company][issue][subIssue]
		if total > 100:
			print (company + " " + str (total))
			for issue in complaints[company]:
				for subIssue in complaints[company][issue]:
					fraction = complaints[company][issue][subIssue]/total
					if fraction >= .1:
						print ("\t" + issue + ", " + subIssue + " " + str(fraction) )
