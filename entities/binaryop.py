from ast import AST


class BinaryOp(AST):
    def __init__(self, op=None, left=None, right=None):
        self.left = left
        self.token = self.op = op
        self.right = right
