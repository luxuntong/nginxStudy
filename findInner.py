#listdir.py
import os 
import sys
import re
def findLine(fileName, pat):
	pattern = re.compile('nginx-1.6.0/(.+)$')
	strPat = pattern.search(pat)
	inner = re.compile(strPat.group(1))
	fileRead = open(fileName, 'r')
	listRead = fileRead.readlines()
	for i in range(len(listRead)):
		strFind = inner.search(listRead[i])
		if(strFind):
			print(strPat.group(1))
			print(i)
		

def findInner(fileName, inner):
	pattern = re.compile(inner)
	fileRead = open(fileName, 'r')
	for line in fileRead:
		strFind = pattern.search(line)
		if(strFind):
			return True
	return False

def listyoudir(level, path, inner, lineFile): 
	pattern = re.compile(inner)
	for i in os.listdir(path): 
#		print ('     '*(level+1) + i)
		if os.path.isdir(path + '/' + i):
#			print ('     '*(level+1) + i)
			listyoudir(level+1, path + '/' + i, inner, lineFile)
		else:
			if (findInner(path + '/' + i, inner)):
				print(path + '/' + i)
				findLine(lineFile, path + '/' + i)

if (len(sys.argv) == 2 and sys.argv[1] == '-h'):
	print('the first argv is path')
	print('the second argv is inner which you want to search')
elif (len(sys.argv) == 4):
	listyoudir(0, sys.argv[1], sys.argv[2], sys.argv[3])


