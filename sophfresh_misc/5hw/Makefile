
# this is a gnu-extension.  Don't worry about it.  Delete it, if you're
# not using gnu-make
.PHONY : run test_post problem1

# run will call your test_post target, below
run : test_post

# we need this target to grade.  We will supply our own input.
problem1 : problem1.py
	python problem1.py

# if you also submit a file called sample-problem1.input, then this target
# will be run automatically by the submit wrapper, so you can see it
# working
test_post : problem1.py
	python problem1.py 
