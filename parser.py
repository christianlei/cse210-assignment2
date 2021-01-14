from entities.binaryop import BinaryOp
from entities.item import Item


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Parser:
    def __init__(self, parsed_string):
        self.ast = None
        self.parsed_list = parsed_string.split(' ')

    def string_to_AST(self):
        ast = None
        while self.parsed_list:
            item = self.parsed_list.pop(0)
            if item == ':=':
                bin_op = BinaryOp(ast, ':=', Item('INT', self.parsed_list.pop(0)))
                ast = bin_op
            elif represents_int(item):
                ast = Item('Int', item)
            else:
                ast = Item('Var', item)
        self.ast = ast

    # def string_to_AST(self):
    #     ast = None
    #     while self.parsed_list:
    #         item = self.parsed_list.pop(0)
    #         if item == '+':
    #             bin_op = BinOp(ast, '+', Num('int', self.parsed_list.pop(0)))
    #             ast = bin_op
    #         elif item == '-':
    #             bin_op = BinOp(ast, '-', Num('int', self.parsed_list.pop(0)))
    #             ast = bin_op
    #         elif item == '*':
    #             if isinstance(ast, BinOp) and (ast.op == '+' or ast.op == '-'):
    #                 mult_node = BinOp(
    #                     ast.right, '*', Num('int', self.parsed_list.pop(0)))
    #                 ast.right = mult_node
    #             else:
    #                 bin_op = BinOp(
    #                     ast, '*', Num('int', self.parsed_list.pop(0)))
    #                 ast = bin_op
    #         else:
    #             num = Num('int', item)
    #             ast = num

    #     self.ast = ast
