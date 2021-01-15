# from entities.binaryop import BinaryOp
# from entities.item import Item
#
#
# def represents_int(item):
#     try:
#         int(item)
#         return True
#     except ValueError:
#         return False
#
# def determine_unary_item(item):
#     if item == 'true':
#         return Item('TRUE', True)
#     elif item == 'false':
#         return Item('FALSE', False)
#     elif represents_int(item):
#         return Item('INT', item)
#     else:
#         return Item('VAR', item)
#
#
# class Parser:
#     def __init__(self, parsed_string):
#         self.ast = None
#         self.parsed_list = parsed_string.split(' ')
#
#     def string_to_AST(self):
#         ast = None
#         while self.parsed_list:
#             item = self.parsed_list.pop(0)
#             if item == ':=':
#                 bin_op = BinaryOp(ast, ':=', Item('INT', self.parsed_list.pop(0)))
#                 ast = bin_op
#             elif item == 'skip':
#                 continue
#             elif item == "if":
#             elif item == "then":
#             elif item == "else":
#             else:
#                 ast = determine_unary_item(item)
#         self.ast = ast
#
