#!/usr/bin/python

#import cell
import sys




def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)



    

def main( argv=sys.argv ) :
	"Just a test driver - NOT part of the class"

	c = fib(int(argv[1]))
	print str(c)
	
	

if __name__ == "__main__" :
	# then this was NOT included in another file, so, run the test driver
	main()

