import sys
import csv
import random


def distNoRoot(a,b):
	num_fields = len(a)
	dist = 0
	for i in range(0, num_fields):
		dist += (a[i] - b[i]) * (a[i] - b[i])
	return dist
	
def printArray(array):
	for row in array:
		print(row)
	print("")

with open(sys.argv[1], "r") as in_file_raw:
	num_groups = int(sys.argv[2])
	in_file = csv.reader(in_file_raw)
	data_string = list(in_file)
	num_fields = len(data_string)
	num_attributes = len(data_string[1])
	data = []
	for i in range(0,num_fields):
		data.append([])
		for j in range(0,num_attributes):
			data[i].append(float(data_string[i][j]))
		data[i].append(-1)
	printArray(data)
	print(num_groups)
	print(num_fields)
	print(num_attributes)
	means_start = random.sample(range(0, num_fields), num_groups)
	means = []
	for i in means_start:
		means.append(data[i])
	printArray(means_start)
	printArray(means)
	iterations = 0
	while True:
		iterations += 1
		print("Iterations: " + str(iterations))
		diff = False
		# assign points to groups
		for point in data:
			i = -1
			new_mean = -1
			dist = sys.float_info.max
			for mean in means:
				i += 1
				new_dist = distNoRoot(mean, point)
				if new_dist < dist:
					new_mean = i
					dist = new_dist
				print(str(new_dist) + " " + str(i))
			if point[-1] != new_mean:
				point[-1] = new_mean
				diff = True
		print("new points:")
		printArray(data)
		# recalculate means
		for i in range(0, num_groups):
			num_points = 0
			for j in range(0,num_attributes):
				means[i][j] = 0
			for point in data:
				if point[-1] == i:
					num_points += 1
					for j in range(0,num_attributes):
						means[i][j] += point[j]
			if not num_points == 0:
				for j in range(0,num_attributes):
					 means[i][j] = means[i][j]/num_points
		print("New means: ")
		printArray(means)
		if not diff:
			break
		
