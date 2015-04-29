import sys



    
        
def downheap( array, pos ):
    if pos <= ( len(array) - 1) / 2 :
        L = 2*int(pos) + 1
    
        if L == len(array) - 1:
            if array[L] > array[pos]:
                temp = array[pos]
                array[pos] = array[L]
                array[L] = temp
                #array[pos], array[L] = swap( array[pos], array[L] )

        else:   
            R = L + 1

            if array[L] > array[R] :
                            if array[L] > array[pos]:
                                    temp = array[pos]
                                    array[pos] = array[L]
                                    array[L] = temp
                                    downheap( array, L)
                    

            elif array[R] > array[L] :
                if array[R] > array[pos]:
                                    temp = array[pos]
                                    array[pos] = array[R]
                                    array[R] = temp
                                    downheap( array, R )       

def make_heap(Array):
    L = int(((len(Array)-1)-1)/2)
    while (L >= 0):
        downheap (Array , L)
        L=L-1

def swap( a, b ) :
    return b,a


def start():
    Arr = [0,1,2,3,4,5,6,7,8,9,10]
    for i in range(0, len(Arr)):
        print (Arr[i])
            
    make_heap(Arr)
    print ("---")

    for i in range(0, len(Arr)):
        print (Arr[i])


if __name__ == "__main__":
    start()
