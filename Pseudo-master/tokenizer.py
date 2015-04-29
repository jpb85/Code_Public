import string
import re

integer_pattern = re.compile("\\A\\-?\\d+\\Z")
identifier_pattern = re.compile("\\A[a-zA-z]+\\d*\\Z")

class Token:

    TYPE_OPERATOR = 0
    TYPE_PAREN = 1
    TYPE_INTEGER = 2
    TYPE_BOOLEAN = 3
    TYPE_KEYWORD = 4
    TYPE_IDENTIFIER = 5

    def __init__(self, s):

        self.value = s

        if s in {"+","-","*","/","%","=","<",">","==","!=","<=",">=","not","and","or", "\n"}:
            self.type = self.TYPE_OPERATOR
        elif s in {"(",")"}:
            self.type = self.TYPE_PAREN
        elif integer_pattern.match(s):
            self.type = self.TYPE_INTEGER
            self.value = int(s)
        elif s in {"True","False"}:
            self.type = self.TYPE_BOOLEAN
            if s == "True":
                self.value = True
            elif s == "False":
                self.value = False
        elif s in {"if","while","done"}:
            self.type = self.TYPE_KEYWORD
        elif identifier_pattern.match(s):
            self.type = self.TYPE_IDENTIFIER
        else:
            raise Exception("Invalid token: {0}".format(s))
    
class Tokenizer:

    #newlines are part of the language
    sep = "\t\r\v\f " #tab, carraige return, vertical tab, form feed

    def __init__(self, s):
        self.s = s
        self.index = 0
        self.next_tokens = []

    def initialize_next_tokens(self, n):
        if self.next_tokens and self.next_tokens[-1] == None:
            return

        while len(self.next_tokens) < n:
            while self.index < len(self.s) and self.s[self.index] in self.sep:
                self.index += 1  #consume seperator before token

            if self.index == len(self.s):
                self.next_tokens.append(None)
                continue

            current_token = self.s[self.index]
            self.index += 1

            if current_token in string.punctuation+"\n" and current_token != ")": 
                delimiters = string.whitespace + string.ascii_letters + string.digits +"("
            else:
                delimiters = string.whitespace + string.punctuation

            while self.index < len(self.s) and self.s[self.index] not in delimiters:
                current_token += self.s[self.index]
                self.index += 1 #consume everything before next seperator
                                #that's our token

            self.next_tokens.append(Token(current_token))
        
    def peek(self,n=1):
        self.initialize_next_tokens(n)

        if len(self.next_tokens) >= n:
            return self.next_tokens[n-1]
        else:
            return None

    def get_next_token(self):
        self.initialize_next_tokens(1)
        next_token = self.next_tokens[0]

        self.consume()

        return next_token

    def consume(self):
       # if self.next_tokens[0]:
        #    print self.next_tokens[0].value
        self.next_tokens = self.next_tokens[1:]
