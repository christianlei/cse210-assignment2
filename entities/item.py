from ast import AST


class Item(AST):
    def __init__(self, token, value):
        self.token = token
        self.value = value
