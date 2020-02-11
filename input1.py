from sys import argv

if len(argv) == 1:
    print("type argument/file name")
else:
    filename = argv[1]
    try:
        with open(filename) as file:
            info = file.read()
    except IOError:
        print("No file has found such name")
    else:
        file = open(filename, "r")
        #Array = file.readlines()
        #Array1 = file.readline() - String

        print(Array1)
        
        Array2 = file.readline()
        #for line in range(len(Array)):
         #   for list1 in list2:
          #      add list1 to list2 

        a1 = {Array1}
        a2 = {Array2}
      
        print('A =', '{',a1,'}')
        print('B =', a2)
        print(Array)

        #array 
        #split the line


          
        