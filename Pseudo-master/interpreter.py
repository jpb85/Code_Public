import sys
from parser import *
from tokenizer import *

env = dict()

if len(sys.argv) >= 2:
    script_file = open(sys.argv[1], 'r')
    code = script_file.read()
    program = parse(code)
    program.eval(env)
    print env
else:
    line = ""
    while line != "exit":
        line = raw_input()
        tokens = Tokenizer(line)
        next_statement = statement(tokens)
        result = next_statement.eval(env)
        if result != None:
            print result
