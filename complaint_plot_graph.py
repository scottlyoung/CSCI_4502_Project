import csv
import matplotlib.pyplot as plt
import sys
import numpy as np




dateList = []
with open(sys.argv[1], "r") as input_File:

		#This just skips the header line in the csv file
	next(input_File)
	
	date_dict = {}

	readcsv = csv.reader(input_File)
	listcsv = list(readcsv)

	


	for g in listcsv:
		date =  g[0][6:]+ ","+g[0][:2]
		if date not in dateList:
			dateList.append(date)

dateList.sort()

with open(sys.argv[1], "r") as input_File:


	next(input_File)
	
	issue_dict = {}
	
	
	

	readcsv = csv.reader(input_File)
	listcsv = list(readcsv)

	

	for g in listcsv:
		date =  g[0][6:]+ ","+g[0][:2]
		issue = g[1]
		datenum = [i for i,x in enumerate(dateList) if x == date][0]
		
		if issue not in issue_dict:
		
			issue_dict[issue] = []

			for x in dateList:
				issue_dict[issue].append(0)
				
			issue_dict[issue][datenum] =  1
					
		else:
			
			issue_dict[issue][datenum] = issue_dict[issue][datenum] + 1	

	dateList.pop()
	dateList.pop()
	for d in issue_dict:
		issue_dict[d].pop()
		issue_dict[d].pop()

		mark = plt.plot(issue_dict[d], label = d)
	
	plt.legend(loc = "upper right")
	plt.ylabel("Occurrences")
	plt.xlabel("Year, Month")
	plt.grid(color = 'b', linestyle='-',linewidth = 0.1)
	plt.show()

		
		
