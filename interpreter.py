from entities.binaryop import BinaryOp
from entities.item import Item


class Interpreter:

    def __init__(self):
        self.d = {}

    def eval(self, ast):
        if isinstance(ast, BinaryOp):
            if ast.op == ':=':
                self.d[self.eval(ast.left)] = self.eval(ast.right)

        if isinstance(ast, Item):
            if ast.token == 'INT':
                return int(ast.value)
            else:
                return ast.value

    def dictionary_to_result(self):
        string_format = '{0} → {1}'
        return_list = []
        for key, value in self.d.items():
            return_list.append(string_format.format(key, value))
        return_string = " ,".join(return_list)
        final_result = '{' + return_string + '}'
        print(final_result)
