from parser import Parser
from interpreter import Interpreter


def main():
    val = input()
    parser = Parser(val)
    interpreter = Interpreter()

    interpreter.dictionary_to_result()


if __name__ == '__main__':
    main()
