import os
import filecmp
import csv
import operator
from dateutil.relativedelta import *
from datetime import date


def getData(file):
	inFile = csv.DictReader(open(file, 'r'))
	lines = []
	for row in inFile:
		lines.append(row)
	return (lines)
	pass

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	dataSorted = sorted(data, key = lambda i: i[col])
	return (dataSorted[0]['First'] + " " + dataSorted[0]['Last'])
	pass


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	size = {'Freshman':0, 'Sophomore':0, 'Junior':0, 'Senior':0} 
	for row in data:
		size[row['Class']] += 1
	return sorted(size.items(), key = lambda x: x[1], reverse = True)
	pass


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data
	months = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

	for col in a:
		line = col['DOB']
		values = line.split('/')
		month = int(values[0])
		months[month] += 1
	maxValueKey = max(months.items(), key = operator.itemgetter(1))[0]
	return maxValueKey
	pass 

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as first,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	
    csvfile = open(fileName, 'w')
    dataSorted = sorted(a, key = lambda i: i[col])
    for student in dataSorted:
    	first = student['First']
    	last = student['Last']
    	email = student['Email'] 
    	csvfile.write(first + ',' + last + ',' + email + '\n')
    pass

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	currentDate = date.today()
	total_age = 0
	num_rows = 0
	for col in a:
		date_of_birth = col['DOB']
		values = date_of_birth.split('/')
		year = int(values[2])
		age = currentDate.year - year
		num_rows += 1
		total_age += age
	average_age = int(total_age/num_rows)
	return average_age 

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()

