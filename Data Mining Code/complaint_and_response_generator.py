#!/usr/bin/python

import sys
import csv
'''
Author: Michael Min
Date: 3/17/2017

This python file is made to collect 200 entries: 100 that 
have words in the "Consumer Complaint Narrative" attribute
and 100 that have words in the "Company public response"
attribute. The output data will be used as training data for algorithms

To activate, run the following command:

python3 complaint_and_response_generator.py Consumer_Complaints.csv 

The following two files will be output:

complaintNarratives.csv companyResponses.csv

'''

#open files here. The two output files will always be "complaintNarratives.csv" (all entries that have words in the Consumer Complaint Narrative attribute) and "companyResponses.csv" (all entries that have words in the Company public response attribute)
with open(sys.argv[1], "r") as input_File, open("complaintNarratives.csv", 'w') as complaints_File, open ("companyResponses.csv", 'w') as responses_File:
	
	#Add header to the new files
	next(input_File)
	complaints_File.write("Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID\n")	
	responses_File.write("Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID\n")	
	
	#Set up csv readers and writers
	readcsv = csv.reader(input_File)
	listcsv = list(readcsv)
	complaint_Writer = csv.writer(complaints_File, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	response_Writer = csv.writer(responses_File, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	
	#set up counters to count up to 100 for each attribute
	complaint_Counter = 0
	response_Counter = 0

	#for every line in the original csv file
	for g in listcsv:
		complaint_Detected = False
		response_Detected = False

		#Consumer Complaint Narrative 
		if (g[5] != ''):
			complaint_Detected = True
			complaint_Counter = complaint_Counter + 1
			
		#Company public response
		if (g[6] != ''):
			response_Detected = True
			response_Counter= response_Counter + 1
		
		#If the correct attributes have words in them, we are allowed to write the entry to the file
		if (complaint_Detected == True and complaint_Counter < 100):
			complaint_Writer.writerow(g)
			
			
		if (response_Detected == True and response_Counter < 100):
			response_Writer.writerow(g)
		
		#If both attributes have detected 100 entries each, we are allowed to leave before reading the whole file
		if (complaint_Counter == 100 and response_Counter == 100):
			break
