#! /usr/bin/python
#jpb85 problem 5
#imports
import random;
import sys;
#set up 
word1 = "\n"
word2 = "\n"
nullword = "\n" 
# create hashtable and read file
hashtable = {}
f = open('log.txt', 'r')#read only
for line in f:
    for word in line.split():
        hashtable.setdefault( (word1, word2), [] ).append(word)
        word1, word2 = word2, word
hashtable.setdefault( (word1, word2), [] ).append(nullword)
# create output and show
word1 = nullword #\n reset
word2 = nullword #\n reset
max = 10000 #max number of words for output
print "start of output from markov chain:";
for i in xrange(max):
    newword = random.choice(hashtable[(word1, word2)])
    if newword == nullword: sys.exit() #end of text
    print newword;
    word1, word2 = word2, newword
	
print "end of output from markov chain:";
	
	

	
	