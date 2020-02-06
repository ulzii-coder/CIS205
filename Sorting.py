import sys
import os

def program(*args):
    # do whatever
    pass

if __name__ == "__main__":
    try:
        arg1 = sys.argv[1]
        print(arg1)
    except IndexError:
        print "command line parameter is missing"
        sys.exit(1)

    # start the program
    program(arg1)