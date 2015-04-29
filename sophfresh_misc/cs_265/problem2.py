#!/usr/bin/python


import sys
import io


def printlist( X):
    while X != None :
        print X.data
        X = X.next
    

 #fib(n) {
 #   if n is 1 or 2, return 1;
 #   if memo[n] is not zero, return memo[n];
 #   memo[n] = fib(n-1) + fib(n-2);
 #   return memo[n];
 # }


memo = [0]*101 

def fibmemoization  (n) :
    if n == 1 :  
        return 1
    if  n == 2:
        return 1
    if memo[n] != 0 :
        return memo [n]
    memo[n] = fibmemoization(n-1) + fibmemoization(n-2)
    return memo[n]
    


    

    
                
    

def main( argv=sys.argv ) :
	"Just a test driver - NOT part of the class"
        c = fibmemoization(int(argv[1]))
        print str(c)

        
	
	

if __name__ == "__main__" :
	# then this was NOT included in another file, so, run the test driver
	main()

