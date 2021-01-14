from parser import Parser
from interpreter import Interpreter


def main():
    val = input()
    parser = Parser(val)
    parser.string_to_AST()

    interpreter = Interpreter()
    interpreter.eval(parser.ast)
    interpreter.dictionary_to_result()
    return


if __name__ == '__main__':
    main()
