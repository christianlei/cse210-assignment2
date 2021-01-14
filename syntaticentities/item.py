from ast import AST


class Item(AST):
    def __init__(self, token, value, entity_type):
        self.token = token
        self.value = value
        self.entity_type = entity_type
