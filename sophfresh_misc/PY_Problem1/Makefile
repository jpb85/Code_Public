
# this is a gnu-extension.  Don't worry about it.  Delete it, if you're
# not using gnu-make
.PHONY : run test_post fuck

# run will call your test_post target, below
run : test_post

# we need this target to grade.  We will supply our own input.
fuck : prob1.py
	python make_heap2.py

# if you also submit a file called sample-make_heap2.input, then this target
# will be run automatically by the submit wrapper, so you can see it
# working
test_post : prob1.py
	python prob1.py 
