from entities.operator import BinaryOp, Expression, MultiExpression
from entities.item import Int, NegInt, Var, Bool


class Interpreter:

    def __init__(self):
        self.d = {}
        self.empty_var = 0

    def check_in_dict(self, var):
        if var in self.d:
            return self.d[var]
        return self.empty_var

    def eval(self, item):
        if isinstance(item, MultiExpression):
            self.eval(item.first)
            if item.next is not None:
                self.eval(item.next)

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
            if item.op == '∧':
                return self.eval(item.left) and self.eval(item.right)
            if item.op == '∨':
                return self.eval(item.left) or self.eval(item.right)

            left_item = self.eval(item.left)
            right_item = self.eval(item.right)
            if isinstance(left_item, int) and isinstance(right_item, int):
                if item.op == '=':
                    return left_item == right_item
                if item.op == '<':
                    return left_item < right_item
            if isinstance(left_item, str) and isinstance(right_item, str):
                self.check_in_dict(left_item)
                self.check_in_dict(right_item)
                if item.op == '=':
                    return self.check_in_dict(left_item) == self.check_in_dict(right_item)
                if item.op == '<':
                    return self.check_in_dict(left_item) < self.check_in_dict(right_item)
            if isinstance(right_item, str) and isinstance(left_item, int):
                self.check_in_dict(right_item)
                if item.op == '=':
                    return left_item == self.check_in_dict(right_item)
                if item.op == '<':
                    return left_item < self.check_in_dict(right_item)
            if isinstance(right_item, int) and isinstance(left_item, str):
                if item.op == '=':
                    return right_item == self.check_in_dict(left_item)
                if item.op == '<':
                    return  self.check_in_dict(left_item) < right_item
            # if item.op == '¬':
            #     return not self.eval(item.right)

        if isinstance(item, Int) or isinstance(item, NegInt):
            return item.value
        elif isinstance(item, Var):
            return item.value
        elif isinstance(item, Bool):
            return item.value
        return

    def dictionary_to_result(self):
        string_format = '{0} → {1}'
        return_list = []
        for key, value in self.d.items():
            return_list.append(string_format.format(key, value))
        return_string = " ,".join(return_list)
        final_result = '{' + return_string + '}'
        print(final_result)
