from binaryop import BinaryOp
from item import Item


class Interpreter:

    def __init__(self):
        self.d = {}

    def eval(self, ast):
        if isinstance(ast, BinaryOp):
            if ast.op == ':=':
                return dict[self.eval(ast.left)] = self.eval(ast.right)

        if isinstance(ast, Num):
            return int(ast.value)

    def dictionary_to_result(self):
        string_format = '{0 → 1}'
        string_brackets = '{{0}}'
        return_list = []
        for (key, values) in self.d.items():
            for value in values:
                return_list.append(string_format.format(key, value))
        return_string = " ,".join(return_list)
        print(string_brackets.format(return_string))
