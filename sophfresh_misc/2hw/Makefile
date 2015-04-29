
# this is a gnu-extension.  Don't worry about it.  Delete it, if you're
# not using gnu-make
.PHONY : run test_post post

# run will call your test_post target, below
run : test_post

# we need this target to grade.  We will supply our own input.
post : post.py
	python post.py

# if you also submit a file called sample-post.input, then this target
# will be run automatically by the submit wrapper, so you can see it
# working
test_post : post.py
	python post.py < sample-post.input
