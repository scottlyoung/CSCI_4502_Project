import sys
import csv
'''
Author: Michael Min
Date: 3/13/2017

This python file is made to clean up the consumer complaint database.
It searches primarily for empty cells that are from non-optional 
attributes and attempts to remedy them by posting an "UNKNOWN" value 
instead of a blank space. It also searches down the nominal attributes 
and marks any values that are not expected as "INVALID ENTRY".

To activate, run the following command:

python3 cleanUp.py Consumer_Complaints.csv [new_filename].csv

'''

#open file here
with open(sys.argv[1], "r") as inputFile, open(sys.argv[2], 'w') as outputFile:
	
	#Add header to cleaned file
	next(inputFile)
	outputFile.write("Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID\n")	
	
	#Set up csv readers and writers
	readcsv = csv.reader(inputFile)
	listcsv = list(readcsv)
	cleanWriter = csv.writer(outputFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

	#for every line in the original csv file
	for g in listcsv:

		#Date recieved
		if (g[0] == ''):
			g[0] = "UNKNOWN"
		
		#Product
		if (g[1] == ''):
			g[1] = "UNKNOWN"
				
		#Issue
		if (g[3] == ''):
			g[3] = "UNKNOWN"
		
		#Company	
		if (g[7] == ''):
			g[7] = "UNKNOWN"
		
		#State		
		if (g[8] == ''):
			g[8] = "UNKNOWN"
		
		#ZIP code
		if (g[9] == ''):
			g[9] = "UNKNOWN"
			
		#Consumer consent provided?
		if (g[11] != '' and g[11] != "N/A" and g[11] != "Consent withdrawn" and g[11] != "Consent provided" and g[11] != "Consent not provided" and g[11] !="Other"):
			g[11] = "ERROR"
		
		#Consumer consent provided?
		if (g[11] == ''):
			g[11] = "UNKNOWN"
		
		#Submitted via		
		if (g[12] != '' and g[12] != "Email" and g[12] != "Fax" and g[12] != "Phone" and g[12] != "Postal Mail" and g[12] !="Referral" and g[12] !="Web"):
			g[12] = "ERROR"

		#Submitted via
		if (g[12] == ''):
			g[12] = "UNKNOWN"
				
		#Date sent to company
		if (g[13] == ''):
			g[13] = "UNKNOWN"
			
		#Timely Response?
		if (g[15] != '' and g[15] != 'Yes' and g[15] != 'No'):
			g[15] = "ERROR"
		
		#Timely Response?
		if (g[15] == ''):
			g[15] = "UNKNOWN"
			
		#Consumer disputed?
		if (g[16]== ''):
			g[16] = "UNKNOWN"
			
		#Complaint ID
		if (g[17] == ''):
			g[17] = "UNKNOWN"

		#Write them all to the cleaned file
		cleanWriter.writerow(g)
	
