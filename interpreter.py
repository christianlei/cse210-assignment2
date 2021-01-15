from entities.binaryop import BinaryOp
from entities.item import Item


class Interpreter:

    def __init__(self):
        self.d = {}

    def eval(self, item):
        if isinstance(item, BinaryOp):
            if item.op == ':=':
                self.d[self.eval(item.left)] = self.eval(item.right)
            if item.op == '+':
                return self.eval(item.left) + self.eval(item.right)
            if item.op == '*':
                return self.eval(item.left) * self.eval(item.right)
            if item.op == '-':
                return self.eval(item.left) - self.eval(item.right)
            if item.op == '=':
                return self.eval(item.left) == self.eval(item.right)
            if item.op == '<':
                return self.eval(item.left) < self.eval(item.right)
            if item.op == '^':
                return self.eval(item.left) and self.eval(item.right)
            if item.op == 'v':
                return self.eval(item.left) or self.eval(item.right)
            if item.op == '¬':
                return not self.eval(item.right)

        if isinstance(item, Item):
            if item.token == 'INT':
                return int(item.value)
            elif item.token == 'TRUE':
                return item.value
            elif item.token == 'FALSE':
                return item.value
            else:
                return item.value

    def dictionary_to_result(self):
        string_format = '{0} → {1}'
        return_list = []
        for key, value in self.d.items():
            return_list.append(string_format.format(key, value))
        return_string = " ,".join(return_list)
        final_result = '{' + return_string + '}'
        print(final_result)
