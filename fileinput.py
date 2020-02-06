from sys import argv

def countNum(filename):

    #notFoundFile exception
    try:

		#open the file    
		file = open(filename)
		
		
			
			#parts = line.split(",")
		#counter for total number of eights
		
		firstWord = file.readline()
		#get file and return them as string
		for line in file:	
			line = line.rstrip()
			lineList = line.split()
			if(len(lineList)==1):
				print("one word")
			

			for i in line:			
				#check every one of the chars with 8
				if firstWord in "he" or "she" or "they" or "what" or "where" or "where" or "why" or "when" or "who" or "?":
					#if so increment counter
					print("one word")
					
		

		#file not found error
	except IOError:
		print("File not found")


# no argument error	
if len(argv) < 2:
	print "Please include a file name"
	exit()

	
		
countNum(argv[1])

