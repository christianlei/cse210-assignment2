from entities.binaryop import BinaryOp
from entities.item import Item


class Interpreter:

    def __init__(self):
        self.d = {}

    def eval(self, ast):
        if isinstance(ast, BinaryOp):
            if ast.op == ':=':
                self.d[self.eval(ast.left)] = self.eval(ast.right)
            if ast.op == '+':
                return self.eval(ast.left) + self.eval(ast.right)
            if ast.op == '*':
                return self.eval(ast.left) * self.eval(ast.right)
            if ast.op == '-':
                return self.eval(ast.left) - self.eval(ast.right)
            if ast.op == '=':
                return self.eval(ast.left) == self.eval(ast.right)
            if ast.op == '<':
                return self.eval(ast.left) < self.eval(ast.right)
            if ast.op == '^':
                return self.eval(ast.left) and self.eval(ast.right)
            if ast.op == 'v':
                return self.eval(ast.left) or self.eval(ast.right)
            if ast.op == '¬':
                return not self.eval(ast.right)

        if isinstance(ast, Item):
            if ast.token == 'INT':
                return int(ast.value)
            elif ast.token == 'TRUE':
                return ast.value
            elif ast.token == 'FALSE':
                return ast.value
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
