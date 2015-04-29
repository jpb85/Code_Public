#!/use/bin/env python
from lexer import *
from math import log
expr =[]


def RadSort(nums,ht,n):
    if n<5:
        for i in range(len(nums)):
            index = nums[i]%pow(256,n)
            index = index / pow(256, n-1)
            ht[index].append(nums[i])
        nums = []
        for i in range(len(ht)):
            for j in range(len(ht[i])):
                nums.append(ht[i][j])
        ht = [[] for i in range(256)]
        n=n+1
        nums = RadSort(nums,ht,n)
    return nums
        
                

def start():
        nums = []
        tnums = []
        INF = 1e308
        size = 0
        global expr
        while get_expression():
                L = []
                TokenS = get_next_token()
                size = size + 1
                while TokenS:
                        L.append(TokenS)
                        TokenS = get_next_token()
                expr.append(L)
        for x in expr:
            for y in x:
                if y != ' ' and y != '\t' :
                    nums.append(int(y))
                    tnums.append(int(y))
        print 'before:'
        print
        print nums
        print'after:'
        print
        ht = [[] for i in range(256)]
        passes = 1
        newL = RadSort(nums,ht,passes)
        print newL
        for x in newL:
            print x

if __name__ == "__main__":
        start()

