import sys
import csv

def date_to_number:

def date_received(string):
	return [0]
	
def product(string):
	return [0]
	
def subProduct(string):
	return [0]
	
def issue(string):
	return [0]
	
def subIssue(string):
	return [0]
	
def consumer_complaint_narrative(string):
	return [0]
	
def company_public_response(string):
	return [0]
	
def company(string):
	return [0]
	
def state(string):
	return [0]
	
def zip_code(string):
	return [0]
	
def tags(string):
	return [0]
	
def consumer_consent_provided(string):
	return [0]
	
def submitted_via(string):
	return [0]
	
def date_sent_to_company(string):
	return [0]
	
def company_response_to_consumer(string):
	return [0]
	
def timely_response(string):
	return [0]
	
def consumer_disputed(string):
	return [0]
	
def complaint_ID(string):
	return [string]
	


#open file here
with open(sys.argv[1], "r") as inputFile, open(sys.argv[2], 'w') as outputFile:
	
	#Add header to cleaned file
	next(inputFile)
	#outputFile.write("Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID\n")	

	#Set up csv readers and writers
	readcsv = csv.reader(inputFile)
	listcsv = list(readcsv)
	outputWriter = csv.writer(outputFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
	
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
