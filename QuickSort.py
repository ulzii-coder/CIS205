from sys import argv

#finding pivot
def piv(l,r):
    arrayList = Array[r]
    i = p-1 #starting index

    for j in range(l,r):
        if(Array[j] <= arrayList):
            Array[i], Array[j] = Array[j] , Array[i]
    Array[i+1],Array[r] = Array[r], Array[i+1]

    return(i+1)

#sorting function
def quickSort(l, r):
    if (l <r):
        q = piv(l,r)
        quickSort(l, q-1)
        quickSort(q+1, r)

if len(argv) == 1:
    print("type argument/file name")
else:
    filename = argv[1]
    try:
        with open(filename) as file:
            info = file.read()
    except IOError:
        print("No file found has such name")
    else:
        file = open(filename, "r")
        Array = file.readlines()

        for line in range(0, len(Array)):
            Array[line] = int (Array[line])
        r = len(Array)
        quickSort(0, r-1)

        print(Array)
