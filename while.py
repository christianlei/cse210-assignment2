import sys
from antlr4 import *
from dist.WhileLexer import WhileLexer
from dist.WhileParser import WhileParser
from interpreter import Interpreter


def main():
    val = InputStream(input('>'))
    lexer = WhileLexer(val)
    stream = CommonTokenStream(lexer)
    parser = WhileParser(stream)
    ast = parser.expr()

    interpreter = Interpreter()
    interpreter.eval(ast)
    interpreter.dictionary_to_result()
    return


if __name__ == '__main__':
    main()
