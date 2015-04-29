#!/usr/bin/python

class ADT:
	def __init__(self, val, parent=None, elements='0', next=None):
		self.val = val
		self.parent = parent
		self.elements = elements
		self.next = next


def Initialize(Values):
	key = 500
	table1 = [ADT(501)]*key
	for i in range(len(Values)):
		index = Values[i] % key
		temp = table1[index]
		table1[index] = ADT(Values[i], None, 1, temp)
	return table1


def findNode(Tset, val):
	node = Tset[ val % len(Tset) ]
	while node.val != val:
		node = node.next
	return node

def findRoot(node):
	if node.parent == None:
		return node
	else:
		return findRoot(node.parent) 

def PathCompress(Tset, node, root):
	if node.parent.val == root.val:
		return Tset
	else:
		temp = ADT(root.val)
		temp.parent = node.parent
		node.parent = root
		return PathCompress(Tset, temp.parent, root)
	
def Find(Tset, value):
	node = findNode(Tset, value)
	if node.parent == None:
		return value
	else:
		root = findRoot(node)
		newSet = PathCompress(Tset, node, root)
		return root.val

def Merge(Tset, val1, val2):
	r1 = findRoot( findNode(Tset,val1) )
	r2 = findRoot( findNode(Tset,val2) )
	if r1.val != r2.val:
		if r1.elements < r2.elements:
			r1.parent = r2
			r2.elements = r2.elements + r1.elements
			r1.elements = 0
		else:
			r2.parent = r1
			r1.elements = r1.elements + r2.elements
			r2.elements = 0

