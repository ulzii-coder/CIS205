from sys import argv

def countNum(filename):

    #notFoundFile exception
    try:
		#open the file    
		file = open(filename)
		oneWordList = ["he", "she", "they", "what", "where","why", "who", "when"]
		
			
		#parts = line.split(",")
		#counter for total number of eights
		
		#get file and return them as string
		for line in file:	
			#line = line.rstrip()
			lineList = line.split()
               
			if(len(lineList)==1):
				print("not statement")
			
            else:
                for i in lineList:			
				#check every one of the chars with 8
				    if i in oneWordList: #or "she" or "they" or "what" or "where" or "where" or "why" or "when" or "who" or "?":
					#if so increment counter
                        print("not statement")
                    else:
                        print("statement")
    #file not found error
    except IOError:
		print("File not found")


# no argument error	
if len(argv) < 2:
	print "Please include a file name"
	exit()

	
		
countNum(argv[1])

