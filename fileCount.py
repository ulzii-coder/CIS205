from sys import argv

def countNum(filename):

	file = open(filename)
	
	count = 0
	
	for line in file:		
		for char in line:			
			if char in "8":
				count +=1
		
	print count
	
if len(argv) < 2:
	print "Please include a file name"
	exit()

	
		
countNum(argv[1])

