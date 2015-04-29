from lexer import *

class BiTree:
	def __init__(self, Value=None, LeftChild=None, RightChild=None):
		self.Value = Value
		self.LeftChild = LeftChild
		self.RightChild = RightChild 
		
def preorder(tree):
	if tree == None:
		return 
	print tree.Value,
	preorder(tree.LeftChild)
	preorder(tree.RightChild)

def inorder(tree):
	if tree == None:
		return
	inorder(tree.LeftChild)
	print tree.Value,
	inorder(tree.RightChild)
	

def postorder(tree):
	if tree == None:
		return
	postorder(tree.LeftChild)
	postorder(tree.RightChild)
	print tree.Value,

def eval(tree):
	if tree.LeftChild == None:
		return int(tree.Value)
	else:
		if tree.Value == "*":
			return eval(tree.LeftChild) * eval(tree.RightChild)
		elif tree.Value == "/":
			return eval(tree.LeftChild) / eval(tree.RightChild)
		elif tree.Value == "+":
			return eval(tree.LeftChild) + eval(tree.RightChild)
		elif tree.Value == "-":
			return eval(tree.LeftChild) - eval(tree.RightChild)

while get_expression():
	Stack = []
	Token = get_next_token()
	while Token:
		if str.isdigit( Token[0]):
			Stack.append(BiTree(Token))
		else:
			RightChild = Stack.pop()
			LeftChild = Stack.pop()
			Stack.append(BiTree(Token, LeftChild, RightChild ))
		Token = get_next_token()
	TheTree = Stack.pop()

	print "preorder:"
	preorder(TheTree)
	print " " 
	print "inorder:"
	inorder(TheTree)
	print " "
	print "postorder:"
	postorder(TheTree)
	print " "
	
	print "eval:", eval(TheTree) 
