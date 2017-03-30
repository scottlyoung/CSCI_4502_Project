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

def chi_square (val1, val2, val3, N):
	e1 = (val1 * val2)/ N #Top Left
	e2 = (val1 * (N - val2))/N # Bot Left
	e3 = ((N - val1) * val2)/ N #Top Right
	e4 = ((N - val1) * (N - val2))/ N #Bot Right
	
	if (e1 == 0 or e2 == 0 or e3 == 0 or e4 == 0):
		return -101
	
	
	chi = (((val3 - e1)*(val3 - e1))/e1) + (((val1 - val3 - e2)*(val1 - val3 - e2))/e2) + (((val2 - val3 - e3)*(val2 - val3 - e3))/e3) + (((N - val1 - val2 + val3 - e4)*(N - val1 - val2 + val3 - e4))/e4)
	return chi

with open(sys.argv[1], "r") as input_File:
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
	
	if (column1 != "None" and column2 != "None"):
		column1_dict = {}
		column2_dict = {}
		combo_dict = {}
		
		final_dict = {}
		N = 0
		
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
			
		next(input_File)
		
		readcsv = csv.reader(input_File)
		listcsv = list(readcsv)
		
		for g in listcsv:
			if g[c1] in column1_dict:
				column1_dict[g[c1]] = column1_dict[g[c1]] + 1				
			else:
				column1_dict[g[c1]] = 1
			if g[c2] in column2_dict:
				column2_dict[g[c2]] = column2_dict[g[c2]] + 1
			else:
				column2_dict[g[c2]] = 1
			tempstr = g[c1] + "|||||" + g[c2]


			if tempstr in combo_dict:
				combo_dict[tempstr][2] = combo_dict[tempstr][2] + 1
			else:
				combo_dict[tempstr] = [g[c1],g[c2],1]
			N = N + 1
			final_dict[g[c1]] = ["NULL", -100]
			
		for h in combo_dict:


			keynum = combo_dict[h][0]
			col2num = combo_dict[h][1]
			numb = chi_square(column1_dict[keynum], column2_dict[col2num],combo_dict[h][2], N)
			
			if (numb > final_dict[combo_dict[h][0]][1]):
				final_dict[combo_dict[h][0]] = [col2num, numb]
 					
	


		for j in final_dict:
			print (j, final_dict[j])

