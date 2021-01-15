from antlr4 import *
from entities.binaryop import BinaryOp
from entities.item import Item

if __name__ is not None and "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser


# This class defines a complete generic visitor for a parse tree produced by WhileParser.

class WhileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileParser#compileUnit.
    def visitCompileUnit(self, ctx: WhileParser.CompileUnitContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by WhileParser#INFIX.
    def visitINFIX(self, ctx: WhileParser.INFIXContext):
        node = BinaryOp()
        if ctx.OP_ADD():
            node.op = '+'
        elif ctx.OP_SUB():
            node.op = '-'
        elif ctx.OP_MUL():
            node.op = '*'
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node

    # Visit a parse tree produced by WhileParser#PARENGRP.
    def visitPARENGRP(self, ctx: WhileParser.PARENGRPContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by WhileParser#INT.
    def visitINT(self, ctx: WhileParser.INTContext):
        return Item(token='INT', value=str(ctx.NUMBER()))

    # Visit a parse tree produced by WhileParser#UNARY.
    def visitUNARY(self, ctx:WhileParser.UNARYContext):
        if ctx.OP_ADD():
            return self.visit(ctx.expr())
        elif ctx.OP_SUB():
            return Item(token='INT', value=str(ctx.expr()))
        return self.visitChildren(ctx)

del WhileParser