import sys


def downheap(Array,L):
    top = "true"
    T = 0
    while(top == "true"):
        if( T >= len (Array)-1):
            top = "false"
        if (Array[L] > Array[T]):
            temp = Array[L]
            Array[L] = Array[T]
            Array[T] = temp
            top = "false"

        if (Array[2*T + 1] < Array[2*T +2]):
            T = 2*T+1
        else:
            T = 2*T+2

        
            
    path = "true"

    while ( path == "true"):
        if (Array[2*T + 1] < Array[2*T +2]):
            B = 2*T+1
        else:
            B = 2*T+2 
        if( Array[T] < Array[B]):
               temp = Array[L]
               Array[L] = Array[B]
               Array[B] = temp
        else:
            path = "false"
    
        
       

def make_heap(Array):
    L = len(Array)
    while (L >= 0):
        downheap (Array , L)
        L=L-1

Arr = [10,12,13,25,3]
for i in range(0, len(Arr)-1):
    print (Arr[i])
            
make_heap(Arr)


for i in range(0, len(Arr)-1):
    print (Arr[i])
            
