import sys
import csv

'''
Author: Michael Min
Date: 3/27/2017

This python file is made to take in two columns and determine which values
in the second column are the best correlated with the values in the first.
It will run calculations for every unique value in the first column to print the 
three values from the second column with the highest Chi-Square values
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

>python3 Chi_Square_Correlation.py [csv file] [first column] [second column] 

+first column and second column must be one of the following, but cannot 
be the same:

	*prod
	*issue
	*comp
	*state
	*response
'''

#Function for determining chi_square value
def chi_square (val1, val2, val3, N):
	e1 = (val1 * val2)/ N #Top Left
	e2 = (val1 * (N - val2))/N # Bot Left
	e3 = ((N - val1) * val2)/ N #Top Right
	e4 = ((N - val1) * (N - val2))/ N #Bot Right
	
	chi = (((val3 - e1)*(val3 - e1))/e1) + (((val1 - val3 - e2)*(val1 - val3 - e2))/e2) + (((val2 - val3 - e3)*(val2 - val3 - e3))/e3) + (((N - val1 - val2 + val3 - e4)*(N - val1 - val2 + val3 - e4))/e4)
	return chi

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
			
		if column2 == "prod":
			c2 = 1
		elif column2 == "issue":
			c2 = 3
		elif column2 == "comp":
			c2 = 7
		elif column2 == "state":
			c2 = 8
		elif column2 == "response":
			c2 = 14
			
		#This just skips the header line in the csv file
		next(input_File)
		
		#converts the csv file to a more parseable list format
		readcsv = csv.reader(input_File)
		the_csv_file = list(readcsv)
		
		#we iterate through every entry in the csv list
		for entry in the_csv_file:
			
			#Reads in the entry's value at the first attribute. This records the total count of each unique value
			if entry[c1] in column1_dict:
				column1_dict[entry[c1]] = column1_dict[entry[c1]] + 1				
			else:
				column1_dict[entry[c1]] = 1
				
			#Do the same for the second attribute
			if entry[c2] in column2_dict:
				column2_dict[entry[c2]] = column2_dict[entry[c2]] + 1
			else:
				column2_dict[entry[c2]] = 1
				
			#Do the same for combos (when the first attribute value and the second appear together). Get the total count for each unique combo	
			tempstr = entry[c1] + "|||||" + entry[c2]
			if tempstr in combo_dict:
				combo_dict[tempstr][2] = combo_dict[tempstr][2] + 1
			else:
				combo_dict[tempstr] = [entry[c1],entry[c2],1]
				
			#Add 1 to the total entry count
			N = N + 1
			
			#in the final dictionary, store each unique value in column 1. The "NULL" is reserved for the value in the second attribute the correlates best
			#-100 is for the chi-square value between the chosen attribute 1 and 2 values
			final_dict[entry[c1]] = ["NULL", -100]
			
			
			
		#For each combination of attribute 1 and 2 values, iterate and:
		for h in combo_dict:
			
			#Get the total amount of times the first attribute value appears,
			column1_value_count = column1_dict[combo_dict[h][0]]
			
			#the total amount of times the second attribute value appears,
			column2_value_count = column2_dict[combo_dict[h][1]]
			
			#and the total amount of times they appear together
			union_count = combo_dict[h][2]
			
			#determine the chi_square value between them
			correlation_score = chi_square(column2_value_count, column2_value_count,union_count, N)
			
			#If the correlation score's greater than one that the value in attribute 1 currently has, replace it
			if (correlation_score > final_dict[combo_dict[h][0]][1]):
				final_dict[combo_dict[h][0]] = [combo_dict[h][1], correlation_score]
 					

		#Print everything out. We can reformat this later to either print things out in a more readable fashion or write to a text file
		for j in final_dict:
			print (j, final_dict[j])

