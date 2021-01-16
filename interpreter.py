from entities.operator import BinaryOp, Expression
from entities.item import Int, NegInt, Var, Bool


class Interpreter:

    def __init__(self):
        self.d = {}
        self.empty_var = 0

    def eval(self, item):
        if isinstance(item, Expression):
            if self.eval(item.conditional):
                return self.eval(item.true)
            else:
                if item.false is not None:
                    return self.eval(item.false)
                else:
                    return

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
                var = self.eval(item.left)
                if var not in self.d:
                    self.d[var] = self.empty_var
                return self.d[var] == self.eval(item.right)
            # if item.op == '<':
            #     return self.eval(item.left) < self.eval(item.right)
            # if item.op == '^':
            #     return self.eval(item.left) and self.eval(item.right)
            # if item.op == 'v':
            #     return self.eval(item.left) or self.eval(item.right)
            # if item.op == '¬':
            #     return not self.eval(item.right)

        if isinstance(item, Int) or isinstance(item, NegInt):
            return item.value
        elif isinstance(item, Var):
            return item.value
        elif isinstance(item, Bool):
            return item.value

    def dictionary_to_result(self):
        string_format = '{0} → {1}'
        return_list = []
        for key, value in self.d.items():
            return_list.append(string_format.format(key, value))
        return_string = " ,".join(return_list)
        final_result = '{' + return_string + '}'
        print(final_result)
