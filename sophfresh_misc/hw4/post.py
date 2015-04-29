from lexer import *

def preorder(tree):
	temp = tree.val + " "
	if tree.left_child != None:
		temp += preorder(tree.left_child) + " "
	if tree.right_child != None:
		temp += preorder(tree.right_child)
	return temp

def inorder(tree):
	temp = ""
	if tree.left_child != None:
		temp += inorder(tree.left_child) + " "
	temp += tree.val + " "
	if tree.right_child != None:
		temp += inorder(tree.right_child)
	return temp 

def postorder(tree):
	temp = ""
	if tree.left_child != None:
		temp += postorder(tree.left_child) + " "
	if tree.right_child != None:
		temp += postorder(tree.right_child) + " "
	temp += tree.val
	return temp

def eval(tree):
	if tree.left_child == None:
		return int(tree.val)
	else:
		if tree.val == "+":
			return eval(tree.left_child) + eval(tree.right_child)
		elif tree.val == "-":
			return eval(tree.left_child) - eval(tree.right_child)
		elif tree.val == "*":
			return eval(tree.left_child) * eval(tree.right_child)
		else:
			return eval(tree.left_child) / eval(tree.right_child)

class BinaryTree:
	def __init__(self, val=None, left_child=None, right_child=None):
		self.val = val
		self.left_child = left_child
		self.right_child = right_child 

while get_expression():
	expr_stack = []
	t = get_next_token()

	while t:
		if str.isdigit( t[0]):
			expr_stack.append(BinaryTree(t))
		else:
			right_child = expr_stack.pop()
			left_child = expr_stack.pop()
			expr_stack.append(BinaryTree(t, left_child, right_child ))
		t = get_next_token()

	expr_tree = expr_stack.pop()

	print "pre:", preorder(expr_tree)
	print "in:", inorder(expr_tree)
	print "post:", postorder(expr_tree)
	print "eval:", eval(expr_tree) 
