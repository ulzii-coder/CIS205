from sys import argv

def countNum(filename):

    #notFoundFile exception
    try:
		#open the file    
		file = open(filename)
		
			
		#parts = line.split(",")
		m = file.readlines()
        
		
		#get file and return them as string
		for line in file:         
		    

                function sort205(l, r) {
                    if (l < r) {
                            p = divide(p,r);
                            sort205(l, p-1);
                            sort205(p+1, r);
                    }
                }

                function divide(l, r) {
                        x = A[r];
                        i = l-1;

                        for j = l to r-1 {
                                if (A[j] <= x) {
                                        i += 1;
                            exchange A[i] with A[j];
                                }
                        }
                    exchange A[i+1] with A[r]
                        return (i+1);
                }			
				
    except IOError:
		print("File not found")


# no argument error	
if len(argv) < 2:
	print "Please include a file name"
	exit()

	
		
countNum(argv[1])

