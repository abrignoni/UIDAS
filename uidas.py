import argparse
from argparse import RawTextHelpFormatter
import os
from six.moves.configparser import RawConfigParser
import sys

parser = argparse.ArgumentParser(description='Union, intersection, difference, and symmetric difference of the content of 2 text files.')
parser.add_argument("-o",choices=['union', 'intersec', 'diff', 'symmdiff','all'], required=True, help="Comparative operations. See Python 3 Set object methods.")
parser.add_argument('path_to_first_file',help="Path to first file")
parser.add_argument('path_to_second_file',help="Path to second file")

if len(sys.argv[1:])==0:
	parser.print_help()
	# parser.print_usage() # for just the usage line
	parser.exit()
	
args = parser.parse_args()

script_dir = os.path.dirname(os.path.abspath(__file__))
path1 = args.path_to_first_file
path2 = args.path_to_second_file
choice = args.o
uida_version = "120919"

#print(f'{script_dir} {path1} {path2} {choice} {uida_version}')

def unions(file1,file2):
	list1 = open(file1,'r').read().splitlines()
	set1 = set(list1)

	list2 = open(file2,'r').read().splitlines()
	set2 = set(list2)
		
	open('union.txt','w').close()

	with open('union.txt','a') as f:
		resultunion = set1.union(set2)
		print('Items after union: '+ str(len(resultunion)))
		for line in resultunion:
			f.write(line+' \n')

def intersection(file1,file2):
	list1 = open(file1,'r').read().splitlines()
	set1 = set(list1)
	
	list2 = open(file2,'r').read().splitlines()
	set2 = set(list2)
		
	open('intersection.txt','w').close()

	with open('intersection.txt','a') as f:
		resultintersection = set1.intersection(set2)
		print('Items after intersection: ' + str(len(resultintersection)))
		for line in resultintersection:
			f.write(line+' \n')

def symm_diff(file1,file2):
	list1 = open(file1,'r').read().splitlines()
	set1 = set(list1)
	
	list2 = open(file2,'r').read().splitlines()
	set2 = set(list2)
		
	open('symmetric_diff.txt','w').close()

	with open('symmetric_diff.txt','a') as f:
		resultsymmdiff = set1.symmetric_difference(set2)
		print('Items after symmetric difference: ' + str(len(resultsymmdiff)))
		for line in resultsymmdiff:
			f.write(line+' \n')

def difference(file1,file2):
	list1 = open(file1,'r').read().splitlines()
	set1 = set(list1)
	
	list2 = open(file2,'r').read().splitlines()
	set2 = set(list2)
		
	open('difference_file1_to_file2.txt','w').close()

	with open('difference_file1_to_file2.txt','a') as f:
		resultsdifference1 = set1.difference(set2)
		print('Items after difference file 1 - file 2: ' + str(len(resultsdifference1)))
		for line in resultsdifference1:
			f.write(line+' \n')

		
	open('difference_file2_to_file1.txt','w').close()

	with open('difference_file2_to_file1.txt','a') as f:
		resultsdifference2 = set2.difference(set1)
		print('Items after difference file 2 - file 1: ' + str(len(resultsdifference2)))
		for line in resultsdifference2:
			f.write(line+' \n')
print ()
print ('UIDAS: Union, Intersection, Difference, & Symmetric Difference of 2 text files.')
print ('By: @AlexisBrignoni')
print ('Web: abrignoni.com')
print ()
print ('Selected operation/s: '+ choice)

if choice == 'union':
	unions(path1, path2)
elif choice == 'intersec':
	intersection(path1, path2)
elif choice == 'symmdiff':
	symm_diff(path1, path2)
elif choice == 'diff':
	difference(path1, path2)
elif choice == 'all':
	unions(path1, path2)
	intersection(path1, path2)
	symm_diff(path1, path2)
	difference(path1, path2)

print ()
print ('Processing completed.')
	
