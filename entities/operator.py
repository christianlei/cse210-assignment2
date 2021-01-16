from ast import AST


class BinaryOp(AST):
    def __init__(self, op=None, left=None, right=None):
        self.left = left
        self.token = self.op = op
        self.right = right


class Expression(AST):
    def __init__(self, conditional=None, true=None, false=None):
        self.true = true
        self.conditional = conditional
        self.false = false


class MultiExpression(AST):
    def __init__(self, first=None, next=None):
        self.first = first
        self.next = next
