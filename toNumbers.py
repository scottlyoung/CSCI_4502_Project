#!/usr/bin/python

import sys
import csv
import numpy

#def date_to_number:

#converts date to numberr of days since start of 2000, is only aproximate in current state
def stringToDateNum(string):
	nums = string.split("/")
	return ((int(nums[2]) - 2000) * 365) + ((int(nums[1]) - 1) * 30) + int(nums[0])


#open file here
with open(sys.argv[1], "r") as inputFile, open(sys.argv[2], 'w') as outputFile:
	
	#Add header to cleaned file
	next(inputFile)
	#outputFile.write("Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID\n")	

	#Set up csv readers and writers
	readcsv = csv.reader(inputFile)
	listcsv = list(readcsv)
	outputWriter = csv.writer(outputFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	num_rows = len(listcsv)
	num_attributes = len(listcsv[0])
	keys = []
	firstDate = sys.maxsize
	lastDate = 0
	for i in range(0, num_attributes):
		if i == 0:
			keys.append(["Date"])
			for j in range(0, num_rows):
				date = stringToDateNum(listcsv[j][i])
				if firstDate > date:
					firstDate = date
				if lastDate < date:
					lastDate = date 
		elif i == 5:
			keys.append(["Consumer complaint narrative"])
		elif i == 13:
			keys.append(["Date sent to company"])
			for j in range(0, num_rows):
				date = stringToDateNum(listcsv[j][i])
				if firstDate > date:
					firstDate = date
				if lastDate < date:
					lastDate = date 
		elif i == 17:
			keys.append(["Complaint ID"])
		else:
			keys.append([])
			for j in range(0, num_rows):
				if not listcsv[j][i] in keys[i]:
					if not (listcsv[j][i] == "UNKNOWN" or listcsv[j][i] == "ERROR" or listcsv[j][i] == "NONE"):
						keys[i].append(listcsv[j][i])
	date_range = lastDate - firstDate
	header = []
	for row in keys:
		header.extend(row)
	data = numpy.zeros((num_rows, len(header)))
	for i in range(0, num_rows):
		for j in range(0, num_attributes):
			if j == 0:
				data[i][header.index("Date")] = (stringToDateNum(listcsv[i][j]) - firstDate) / date_range
			elif j == 5:
				data[i][header.index("Consumer complaint narrative")] = -1
			elif j == 13:
				data[i][header.index("Date sent to company")] = (stringToDateNum(listcsv[i][j]) - firstDate) / date_range
			elif j == 17:
				data[i][header.index("Complaint ID")] = listcsv[i][j]
			else:
				if not (listcsv[i][j] == "UNKNOWN" or listcsv[i][j] == "ERROR" or listcsv[i][j] == "NONE"):
					data[i][header.index(listcsv[i][j])] = 1
	
	outputWriter.writerow(header)
	for row in data:
		outputWriter.writerow(row)

	'''	
	for i in range(0, num_rows):
		output_data.append([])
		for j in range(0, num_attributes):
			
	output_data = []
	'''		

	'''
	for oldRow in listcsv:
		newRow = []

		newRow.extend(date_recived(oldRow[0]))
		newRow.extend(product(oldRow[1]))
		newRow.extend(subProduct(oldRow[2]))
		newRow.extend(issue(oldRow[3]))
		newRow.extend(subIssue(oldRow[4]))
		newRow.extend(consumer_complaint_narrative(oldRow[5]))
		newRow.extend(company_public_response(oldRow[6]))
		newRow.extend(company(oldRow[7]))
		newRow.extend(state(oldRow[8]))
		newRow.extend(zip_code(oldRow[9]))
		newRow.extend(tags(oldRow[10]))
		newRow.extend(consumer_consent_provided(oldRow[11]))
		newRow.extend(submitted_via(oldRow[12]))
		newRow.extend(date_sent_to_company(oldRow[13]))
		newRow.extend(company_response_to_consumer(oldRow[14]))
		newRow.extend(submitted_via(oldRow[15]))
		newRow.extend(consumer_disputed(oldRow[16]))
		newRow.extend(complaint_ID(oldRow[17]))
			

		#Write them all to the cleaned file
		cleanWriter.writerow(newRow)
	'''
