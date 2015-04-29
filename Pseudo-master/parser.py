from tokenizer import *

class StatementList:
    def __init__(self, statements):
        self.statements = statements

    def eval(self, env):
        for statement in self.statements:
            statement.eval(env)

class IfStatement:
    def __init__(self, conditional_bodies, alternative):
        self.conditional_bodies = conditional_bodies
        self.alternative = alternative

    def eval(self, env):

        for condition,body in self.conditional_bodies:
            cval = condition.eval(env)
            if type(cval) != bool:
                raise Exception("Conditional expressions must be boolean")
 
            if cval:
                body.eval(env)
                break

        if cval == False and self.alternative:
            self.alternative.eval(env)

class WhileStatement:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def eval(self, env):
        cval = self.condition.eval(env)
        if type(cval) != bool:
            raise Exception("Conditional expressions must be boolean")

        while cval: 

            self.body.eval(env)
            cval = self.condition.eval(env)
            if type(cval) != bool:
                raise Exception("Conditional expressions must be boolean") 

class Assignment:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def eval(self, env):
        env[self.name] = self.expression.eval(env)

class Expression:
    
    def __init__(self, first_negation, next_negations):
        self.first_negation = first_negation
        self.next_negations = next_negations

    def eval(self, env):
        cval = self.first_negation.eval(env)
        for junction, negation in self.next_negations:
            nval = negation.eval(env)
            if not( type(cval) == bool and type(nval) == bool):
                raise Exception("Cannot take conjunction or disjunction of non-booleans")
            if junction == "and":
                cval = cval and nval
            elif junction == "or":
                cval = cval or nval

        return cval

class Negation:

    def __init__(self, equivalence):
        self.equivalence = equivalence

    def eval(self, env):
        cval = self.equivalence.eval(env)
        if type(cval) != bool:
            raise Exception("Cannot take negation of non-boolean") 

        return not cval

class Equivalence:

    def __init__(self, first_inequality, next_inequalities):
        self.first_inequality = first_inequality
        self.next_inequalities = next_inequalities

    def eval(self, env):
        cval = self.first_inequality.eval(env)

        for operation, inequality in self.next_inequalities:
            nval = inequality.eval(env)
            if type(cval) != type(nval):
                raise Exception("Cannot compare values of different types")
            
            if operation == "==":
                cval = cval == nval
            elif operation == "!=":
                cval = cval != nval

        return cval

class Inequality:
    def __init__(self, first_expression, operation, next_expression):
        self.first_expression = first_expression
        self.operation = operation
        self.next_expression = next_expression

    def eval(self, env):
        cval = self.first_expression.eval(env)

        if self.operation:
            nval = self.next_expression.eval(env)
            if not( (type(cval) == int or type(cval) == long) and \
                    (type(nval) == int or type(nval) == long) ):
                raise Exception("Can only compare integer values")

            if self.operation == "<":
                cval = cval < nval
            elif self.operation == ">":
                cval = cval > nval
            elif self.operation == ">=":
                cval = cval >= nval
            elif self.operation == "<=":
                cval = cval <= nval

        return cval
            
class ArithmeticExpression: #first_term is an expression, next_terms is a list of tuples of the form (operation,term)
    def __init__(self, first_term, next_terms):
        self.first_term = first_term
        self.next_terms = next_terms

    def eval(self, env):
        cval = self.first_term.eval(env)
        for op,term in self.next_terms:
            nval = term.eval(env)

            if not( ( type(cval) == int or type(cval) == long) and \
                    ( type(nval) == int or type(nval) == long) ):
                raise Exception("Can only add and subtract integers")
  
            if op == "+":
                cval += nval
            elif op == "-":
                cval -= nval

        return cval

class Term:
    def __init__(self, first_factor, next_factors):
        self.first_factor = first_factor
        self.next_factors = next_factors

    def eval(self, env):
        cval = self.first_factor.eval(env)
        for op,factor in self.next_factors:
            nval = factor.eval(env)
            if not(  (type(cval) == int or type(cval) == long) and \
                     (type(nval) == int or type(nval) == long) ):
                raise Exception("Can only multiply or divide integers")

            if op == "*":
                cval *= nval
            elif op == "/":
                cval /= nval
            elif op == "%":
                cval %= nval

        return cval

class Inverse:
    def __init__(self, factor):
        self.factor = factor

    def eval(self, env):
        cval = self.factor.eval(env)
        if not( type(cval) == int or type(cval) == long):
            raise Exception("Can only take the additive inverse of an integer")

        return -cval

class Variable:
    def __init__(self, name):
        self.name = name

    def eval(self, env):
        if self.name in env:
            return env[self.name]
        else:
            raise Exception("{0} is undefined".format(self.name))

class Literal:
    def __init__(self, value):
        self.value = value

    def eval(self, env):
        return self.value

def parse(s):
    tokens = Tokenizer(s)
    return statement_list(tokens)

def statement(tokens):
    next_token = tokens.peek()
    second_token = tokens.peek(2)

    if next_token and next_token.type == Token.TYPE_IDENTIFIER and  \
                    second_token and second_token.value == "=":
        cval = assignment(tokens)
    elif next_token and next_token.value == "if":
        cval = if_statement(tokens)
    elif next_token and next_token.value == "while":
        cval = while_statement(tokens)
    else:
        cval = expr(tokens)

    next_token = tokens.get_next_token()
    if next_token and next_token.value != "\n":
        raise Exception("Expected new line or end of file")

    return cval

def statement_list(tokens):
    next_token = tokens.peek()

    while next_token.value == "\n":
        tokens.consume()
        next_token = tokens.peek()

    statements = []
    while next_token and next_token.value != "done":
        statements.append( statement(tokens) )
        next_token = tokens.peek()

        while next_token and next_token.value == "\n":
            tokens.consume()
            next_token = tokens.peek()

    if next_token:
        tokens.consume()

    return StatementList(statements)

def if_statement(tokens):
    tokens.consume()
    condition = expr(tokens)

    next_token = tokens.get_next_token()
    if not( next_token and next_token.value == "\n"):
        raise Exception("Expected new line")

    body = statement_list(tokens)

    conditional_bodies = [(condition, body)]

    next_token = tokens.peek()
    
    while next_token.value == "elif":
        tokens.consume()
        condition = expr(tokens)
        next_token = tokens.get_next_token()
        if not( next_token and next_token.value == "\n"):
            raise Exception("Expected new line")

        body = statement_list(tokens)

        conditional_bodies.append((condition,body))
        next_token = tokens.peek()

    alternative = None

    if next_token.value == "else":
        tokens.consume()
        next_token = tokens.get_next_token()
        if not( next_token and next_token.value == "\n"):
            raise Exception("Expected new line")

        alternative = statement_list(tokens)
     
    return IfStatement(conditional_bodies,alternative)

def while_statement(tokens):
    tokens.consume()
    condition = expr(tokens)

    next_token = tokens.get_next_token()
    if not( next_token and next_token.value == "\n"):
        raise Exception("Expected new line")

    body = statement_list(tokens)

    return WhileStatement(condition,body)

def assignment(tokens):
    name = tokens.get_next_token()
    tokens.consume()

    return Assignment(name.value, expr(tokens))    

def expr(tokens):
    first_negation = negation(tokens)
    next_token = tokens.peek()

    next_negations = []
    while next_token and next_token.value in {"and","or"}:
        tokens.consume()
        next_negations.append( (next_token.value, negation(tokens) ) )
        next_token = tokens.peek()

    if next_negations:
        return Expression(first_negation, next_negations) 
    else:
        return first_negation

def negation(tokens):
    next_token = tokens.peek()

    if next_token.value == "not":
        tokens.consume()
        return Negation(equivalence(tokens))
    else:
        return equivalence(tokens)

def equivalence(tokens):
    first_inequality = inequality(tokens)
    next_token = tokens.peek()
 
    next_inequalities = []
    while next_token and next_token.value in {"==","!="}:
        tokens.consume() 
        next_inequalities.append( (next_token.value, inequality(tokens) ) )
        next_token = tokens.peek()

    if next_inequalities:
        return Equivalence(first_inequality, next_inequalities)
    else:
        return first_inequality

def inequality(tokens):
    first_expression = arith_expr(tokens)
    next_token = tokens.peek()

    operator = None
    next_expression = None
    if next_token and next_token.value in {"<","<=",">",">="}:
        tokens.consume()
        operator = next_token.value
        next_expression = arith_expr(tokens)

    if operator:
        return Inequality(first_expression, operator, next_expression)
    else:
        return first_expression

def arith_expr(tokens):
    first_term = term(tokens)
    next_token = tokens.peek()

    next_terms = []
    while next_token and next_token.value in {"+","-"}:
        tokens.consume()
        next_terms.append( (next_token.value, term(tokens) ) )
        next_token = tokens.peek()

    if next_terms:
        return ArithmeticExpression(first_term, next_terms)
    else:
        return first_term

def term(tokens):
    first_inverse = inverse(tokens) 
    next_token = tokens.peek()

    next_inverses = []
    while next_token and next_token.value in {"*","/","%"}:
        tokens.consume()
        next_inverses.append( (next_token.value, inverse(tokens) ) )
        next_token = tokens.peek()

    if next_inverses:
        return Term(first_inverse, next_inverses)
    else:
        return first_inverse

def inverse(tokens):
    next_token = tokens.peek()

    if next_token.value == "-":
        tokens.consume()
        return Inverse(factor(tokens))

    return factor(tokens)

def factor(tokens):
    next_token = tokens.get_next_token()

    if not next_token:
        raise Exception("Unexpected end of input")

    if next_token.value == "(":
        ival = expr(tokens)

        next_token = tokens.get_next_token()
        if not( next_token and next_token.value == ")"):
            raise Exception("Excpected ), got {0}".format(next_token.value))

        return ival

    elif next_token.type in {Token.TYPE_INTEGER, Token.TYPE_BOOLEAN}:
        return Literal(next_token.value)

    elif next_token.type == Token.TYPE_IDENTIFIER:
        return Variable(next_token.value)

    raise Exception("Excpected (, number or identifer, got {0}".format(next_token.value))
