#!/usr/bin/python

import random
import timeit
import sys


memo = [0]*101 

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def fibmemoization  (n) :
    if n == 1 :  
        return 1
    if  n == 2:
        return 1
    if memo[n] != 0 :
        return memo [n]
    memo[n] = fibmemoization(n-1) + fibmemoization(n-2)
    return memo[n]
    



def timingit1 (n):
    mytime = timeit.Timer( "  fib("+str(n)+")" ,"from __main__ import fib" )
    delta = mytime.timeit( 1 )
    mytime1 = timeit.Timer( "  fibmemoization("+str(n)+")" ,"from __main__ import fibmemoization" )
    delta1 = mytime1.timeit( 1 )
   # print "1 run of concat copy with lists length of "+str(n)+"  took: " + str( delta ) + " seconds."
    print str(n) + "      " + str(delta) + "      "+ str(delta1)


def timingit2 (n):
    mytime1 = timeit.Timer( "  fibmemoization("+str(n)+")" ,"from __main__ import fibmemoization" )
    delta1 = mytime1.timeit( 1 )
    return delta1
    


def main( argv=sys.argv ) :
	
        print "n   fibnormal fibmemoization"    
        for i in range(1, 31, 1):
            timingit1( i )

        filename = "mydata.txt"
        FILE = open(filename,"w")

        

        for i in range(1, 101, 1):
            x = timingit2( i )
            FILE.write(str(i) + "    " +str(x) + "\n" )

        FILE.close()

        
#delta = mytime.timeit( 5 )
#print "5 runs of bar( 1000000 ) took: " + str( delta ) + " seconds."
        print ''


  
if __name__ == "__main__" :
	# then this was NOT included in another file, so, run the test driver
	main()
