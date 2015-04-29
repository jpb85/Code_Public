#!/usr/bin/env python
#
# Create a file, one expression per line
#	 redirect from standard input:
#		test.py < input
#
# Notes:  We are not making our input bullet-proof.  If it looks like a #,
# then it is
#
#		Operands must be integers
#
#		The parser doesn't handle negative operands
#

from lexer import *

while get_expression():
	t = get_next_token()
	while t:
		if str.isdigit( t[0] ) : # we have a (non-negative) number
			op = 'operand'
		else:
			op = 'operator'
		print 'Got token: ' + t + ' (an ' + op + ')'
		t = get_next_token()
	
	print ''


