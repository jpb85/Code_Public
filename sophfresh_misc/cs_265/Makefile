PYTHON = python
VIEWER = less
x = 30
y = 30

.PHONY: clean run view

problem1 : problem1.py
			$(PYTHON) problem1.py $(x)
			
problem2 : problem2.py
			$(PYTHON) problem2.py $(y)
			
problem3 : problem3.py
			$(PYTHON) problem3.py 
			
run :  problem1 problem2 problem3 view
	

clean :
	- \rm $(outFile) *~ > /dev/null 2>&1
