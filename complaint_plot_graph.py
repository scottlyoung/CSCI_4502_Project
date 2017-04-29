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
	
	
	
	issuelist = []
	readcsv = csv.reader(input_File)
	listcsv = list(readcsv)

	

	for g in listcsv:
		date =  g[0][6:]+ ","+g[0][:2]
		issue = g[1]
		datenum = [i for i,x in enumerate(dateList) if x == date][0]
		
		if issue not in issue_dict:
			issuelist.append(issue)
		
			issue_dict[issue] = []

			for x in dateList:
				issue_dict[issue].append(0)
				
			issue_dict[issue][datenum] =  1
					
		else:
			
			issue_dict[issue][datenum] = issue_dict[issue][datenum] + 1	

	dateList.pop()
	dateList.pop()
	for x in range (0,5):
		
		issue_dict[issuelist[x]].pop()
		issue_dict[issuelist[x]].pop()
		plt.plot(issue_dict[issuelist[x]], label = issuelist[x])
			
			
		
			
	plt.ylim((0,6000))
	plt.ylabel("Occurrences")
	plt.xlabel("Year, Month")
	
	plt.xticks(range(len(dateList)),dateList,rotation = 'vertical')
	
	plt.legend(loc = "upper right")
	plt.title("Occurences of Complaint Types from 2011 to 2017 (Part 1)")
	plt.grid()
	

	

	
	
	
	plt.show()
	
	for x in range (6,len(issuelist) - 1):
		
		issue_dict[issuelist[x]].pop()
		issue_dict[issuelist[x]].pop()
		plt.plot(issue_dict[issuelist[x]], label = issuelist[x])
			
			
		
			
	plt.ylim((0,6000))
	plt.ylabel("Occurrences")
	plt.xlabel("Year, Month")
	
	plt.xticks(range(len(dateList)),dateList,rotation = 'vertical')
	
	plt.legend(loc = "upper right")
	plt.title("Occurences of Complaint Types from 2011 to 2017 (Part 2)")
	plt.grid()
	plt.show()
		
		
