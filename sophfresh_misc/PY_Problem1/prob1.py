#!/usr/bin/python
import sys
import random
import timeit


    
        
def downheap( Arr, pos ):
    if pos <= ( len(Arr) - 1) / 2 :
        L = 2*int(pos) + 1
    
    
        if L == len(Arr) - 1:
            if Arr[L] > Arr[pos]:
                temp = Arr[pos]
                Arr[pos] = Arr[L]
                Arr[L] = temp

        else:   
            other = L + 1
            if (Arr[ L] >  Arr[other]) :
                            if (Arr[ L] > Arr[pos]):
                                    temp = Arr[pos]
                                    Arr[pos] = Arr[L]
                                    Arr[L] = temp
                                    downheap( Arr, L)
                    

                    
            elif (Arr[other] > Arr[L]) :
                if (Arr[other] > Arr[pos]):
                                    temp = Arr[pos]
                                    Arr[pos] = Arr[other]
                                    Arr[other] = temp
                                    downheap( Arr, other )       

def make_heap(Array):
    L = int(((len(Array)-1)-1)/2)
    while (L >= 0):
        downheap (Array , L)
        L=L-1


    
def timingit1 (x,n):
    mytime = timeit.Timer( 'make_heap(' + str(n) +')','from __main__ import make_heap')
    delta = mytime.timeit( 1 )
    print (str(x)+"      " + str(delta))


def start():
    print ("---: Array elements before make_heap")
    Arr = [0,1,2,3,4,5,6,7,8,9,10]
    for i in range(0, len(Arr)):
        print (Arr[i])
            
    make_heap(Arr)
    print ("---: Timing  n   t(n)")
    timingit1(10,Arr)
    print ("---:Array elements after make_heap")
    for i in range(0, len(Arr)):
        print (Arr[i])
    print("---: n    t(n)")
    for x in range(10, 111, 10):
        yy = [0]
        for y in range(0, x, 1):
            xx = [x]
            zz = yy + xx 
        timingit1(x,zz)
        


    

    


if __name__ == "__main__":
    start()
