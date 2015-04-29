#!/usr/bin/env python
from lexer import *

expr = []


def floyd(D, P):
	n = len(D)
	for k in range(n):
		for i in range(n):
			for j in range(n):
				if D[i][k] + D[k][j] < D[i][j]:
					D[i][j] = D[i][k] + D[k][j]
					D[j][i] = D[i][k] + D[k][j]
					P[i][j] = k
					P[j][i] = k


def PrintMax( mat ):
	INFnum = 1e308
	size = len(mat)
	print
	print
	print 
	for i in range(size):
		print 
		for j in range(size):
			if mat[i][j] == INFnum:
				print repr( 'INF' ).rjust(4),
			else:
				print repr( mat[i][j] ).rjust(4),
		print
	print

def start():
        INF = 1e308
        size = 0
        global expr #t
        while get_expression():
                L = []
                TokenS = get_next_token()
                size = size + 1
                while TokenS:
                        L.append(TokenS)
                        TokenS = get_next_token()
                expr.append(L)
        DisMax = []
        PreMax = []

        for i in range(size):
                DisMax.append([INF]*size)
                PreMax.append(['null']*size)

        for x in expr:
                i = 1
                while i <= len(x)-1:
                        DisMax[int(x[0])][int(x[i])]= int(x[i+1])
                        DisMax[int(x[i])][int(x[0])]= int(x[i+1])
                        PreMax[int(x[0])][int(x[i])]= int(x[i])
                        PreMax[int(x[i])][int(x[0])]= int(x[0])
                        i = i+2
        for r in range(size):
                DisMax[r][r]=0

        for i in range(size):
                        print DisMax[i],
                        print 


        print 'after read'
        print '----------'
        print 'Distance Matrix'
        PrintMax (DisMax)
        print
        print 'Predecessor Matrix' 
        PrintMax (PreMax)
        floyd(DisMax,PreMax)
        print 'after floyd'
        print '-----------'
        print 'Distance Matrix'
        PrintMax (DisMax)
        print
        print 'Predecessor Matrix'
        PrintMax (PreMax)

        
if __name__ == "__main__":
        start()
