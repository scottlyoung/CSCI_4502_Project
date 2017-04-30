import sys
import csv
import operator
'''
Author: Michael Min
Date: 3/27/2017

This python file is made to take in two columns and determine which values
in the second column are the best correlated with the values in the first.
It will run calculations for every unique value in the first column to print the 
three values from the second column with the highest lift values
(this will measure which are the best correlated). 

Do be aware, however, that only the nominal attribute columns that have
non-trivial information will be allowed.

These include the following:

	*Product
	*Issue
	*Company
	*State
	*Company Response to Consumer

To activate, run the following command:

>python3 lift_Correlation.py [csv file] [first column] [second column] 

+first column and second column must be one of the following, but cannot 
be the same:

	*prod
	*issue
	*comp
	*state
	*response
'''


with open(sys.argv[1], "r") as input_File:


	#checks to see if the the two attributes (arguments 2 and 3) are valid.
	column1 = "None"
	column2 = "None"  
	if (sys.argv[2] == "prod" or sys.argv[2] == "issue" or sys.argv[2] == "comp" or sys.argv[2] == "state" or sys.argv[2] == "response"):
		column1 = sys.argv[2]
		if (sys.argv[3] == column1):
			print("\nInvalid entry for column 2. Please make sure that the entries for column 1 and column 2 are different.\n")
		elif (sys.argv[3] == "prod" or sys.argv[3] == "issue" or sys.argv[3] == "comp" or sys.argv[3] == "state" or sys.argv[3] == "response"):
			column2 = sys.argv[3]
		elif (column2 == "None"):
			print("\nInvalid Entry for Column 2. Please use the following template: \n\n > python3 Chi_Square_Correlation.py [csv file] [first column] [second column] \n \nWhere [second column] is equal to prod, issue, comp, state, or response.\n")
		
	else:
		print("\nInvalid Entry for Column 1. Please use the following template: \n\n > python3 Chi_Square_Correlation.py [csv file] [first column] [second column] \n \nWhere [first column] is equal to prod, issue, comp, state, or response.\n")


	#If both are valid, we go on
	if (column1 != "None" and column2 != "None"):
		
		
		#column1_dict holds all the unique values in the first attribute and the number of times they appear in the csv file.
		#column2_dict does the same.
		column1_dict = {}
		column2_dict = {}
		
		#combo_dict holds all of the attribute 1 and attribute 2 combinations that appear in the file along with the number of each combination appears.
		combo_dict = {}
		
		#final_dict is for printing which value from attribute 2 is most correlated with attribute 1 at the end. It stores the chi-square value and the most correlated attribute 2 value
		final_dict = {}
		
		#N is the total number of entries
		N = 0
		
		
		#c1 and c2 correspond to the column numbers that correspond to the two selected attributes

		if column1 == "prod":
			c1 = 1
		elif column1 == "issue":
			c1 = 3
		elif column1 == "comp":
			c1 = 7
		elif column1 == "state":
			c1 = 8
		elif column1 == "response":
			c1 = 14
		
		challenger = "CH"
		
		if column2 == "prod":
			c2 = 1
			challenger = "products"
		elif column2 == "issue":
			c2 = 3
			challenger = "issues"
		elif column2 == "comp":
			c2 = 7
			challenger = "companies"
		elif column2 == "state":
			c2 = 8
			challenger = "states"
		elif column2 == "response":
			c2 = 14
			challenger = "responses"

		#This just skips the header line in the csv file
		next(input_File)

		#converts the csv file to a more parseable list format
		readcsv = csv.reader(input_File)
		listcsv = list(readcsv)

		#we iterate through every entry in the csv list	
		for g in listcsv:
			
			#Reads in the entry's value at the first attribute. This records the total count of each unique value
			if g[c1] in column1_dict:
				column1_dict[g[c1]] = column1_dict[g[c1]] + 1				
			else:
				column1_dict[g[c1]] = 1

			#Do the same for the second attribute
			if g[c2] in column2_dict:
				column2_dict[g[c2]] = column2_dict[g[c2]] + 1
			else:
				column2_dict[g[c2]] = 1
				
				
			#Do the same for combos (when the first attribute value and the second appear together). Get the total count for each unique combo	
			tempstr = g[c1] + "|||||" + g[c2]
			
			if tempstr in combo_dict:
				combo_dict[tempstr][2] = combo_dict[tempstr][2] + 1
			else:
				combo_dict[tempstr] = [g[c1],g[c2],1]


			#Add 1 to the total entry count
			N = N + 1
			
			#in the final dictionary, store each unique value in column 1. The "NULL" is reserved for the value in the second attribute the correlates best
			#-100 is for the chi-square value between the chosen attribute 1 and 2 values
			final_dict[g[c1]] = []
			

		#For each combination of attribute 1 and 2 values, iterate and:
		for h in combo_dict:

			#Get the combination's attribute 1 and attribute 2 values
			col1value = combo_dict[h][0]
			col2value = combo_dict[h][1]
			
			#Get the ratios of the counts of those values to the total number of entries
			col1Frac = column1_dict[col1value] / N
			col2Frac = column2_dict[col2value] / N
			combinedFrac = combo_dict[h][2] / N
			
			#Calculate correlation coefficient
			correlation_coefficient = combinedFrac/(col1Frac * col2Frac)
			
			#if the calculated correlation coefficient is greater than the current value's biggest correlation coefficient, replace it

			final_dict[combo_dict[h][0]].append((col2value, correlation_coefficient))
			

	
		
		#Print it all out. We can later change this to print other things (like which two attribute types are negatively correlated)
		for j in final_dict:
			sortdict = dict(final_dict[j])
			worker = sorted(dict(final_dict[j]).items(),key=operator.itemgetter(1))[-5:]
			summ = sum(sortdict.values())
			count = len(sortdict)

			print ("===================")
			
			print ("Average lift correlation for " + challenger + " and \"" + j +"\": ",summ/count)
			
			print ("===================")
			print ("Highest Correlations:")
			for k in reversed(worker):
				print (k[0] + ": "+str(k[1]))


