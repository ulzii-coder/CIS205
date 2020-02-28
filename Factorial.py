import sys

#iteration - a loop repeadly executes until the controlling condition becomes false
def iteration1(n, r):

    iteration1 = 1
    for i in range(1,n+1):
        iteration1 = iteration1 * i # save the results in every execution of the loop  

    fib1 = 1
    for i in range(1,n-r+1):
        fib1 = fib1 * i # save the results in every execution of the loop

    div = iteration1/fib1 
    #print(div)
    print("P(" + str(n) + "," + str(r) + ")" + "using iteration:" +str(div))
    #print(fact)
    #print(fact1)

#iteration2 
def iteration(n,r):
    result = 1
    if(n == 0):
        print(1)
    else:
        for i in range(n-r+1, n+1):
            
            result = result *i # save the results in every execution of the loop

        print("P(" + str(n) + "," + str(r) + ")" + "using iteration:" +str(result))    


#recursion - function calls itself repeadly
def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n-1) #function calls itself

#print(fact(10))

def recursion(n,r):
    factorial = fact(n)/fact(n-r)
    print("P(" + str(n) + "," + str(r) + ")" + "using factorials:" +str(factorial))

if len(sys.argv) == 1:
	print("Error: must supply two numbers, n and r.")
elif len(sys.argv) == 2:
	print ("Error: must supply two numbers, n and r.")
else:
	#iteration1(int(sys.argv[1]), int(sys.argv[2]))
    iteration(int(sys.argv[1]), int(sys.argv[2]))
    recursion(int(sys.argv[1]), int(sys.argv[2]))
