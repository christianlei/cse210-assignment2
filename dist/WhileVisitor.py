from antlr4 import *
from entities.binaryop import BinaryOp
from entities.item import Int, NegInt, Var, Bool

if __name__ is not None and "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser


# This class defines a complete generic visitor for a parse tree produced by WhileParser.

class WhileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileParser#compileUnit.
    def visitCompileUnit(self, ctx: WhileParser.CompileUnitContext):
        return self.visit(ctx.stat())

    # Visit a parse tree produced by WhileParser#INFIX.
    def visitINFIX(self, ctx: WhileParser.INFIXContext):
        node = BinaryOp()
        if ctx.OP_ADD():
            node.op = '+'
        elif ctx.OP_SUB():
            node.op = '-'
        elif ctx.OP_MUL():
            node.op = '*'
        elif ctx.OP_ASGN():
            node.op = ':='
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node

    # Visit a parse tree produced by WhileParser#PARENGRP.
    def visitPARENGRP(self, ctx: WhileParser.PARENGRPContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by WhileParser#INT.
    def visitINT(self, ctx: WhileParser.INTContext):
        return Int(value=int(str(ctx.NUMBER())))

    # Visit a parse tree produced by WhileParser#VAL.
    def visitVAL(self, ctx: WhileParser.VALContext):
        return Var(value=(str(ctx.VAR())))

    # Visit a parse tree produced by WhileParser#BOOL.
    def visitBOOL(self, ctx: WhileParser.BOOLContext):
        if ctx.TRUE():
            return Bool(value=(bool(True)))
        elif ctx.FALSE():
            return Bool(value=(bool(False)))

    # Visit a parse tree produced by WhileParser#UNARY.
    def visitUNARY(self, ctx: WhileParser.UNARYContext):
        if ctx.OP_ADD():
            return self.visit(ctx.expr())
        elif ctx.OP_SUB():
            return NegInt(node=self.visit(ctx.expr()))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by WhileParser#PASS.
    def visitPASS(self, ctx: WhileParser.PASSContext):
        return

    # Visit a parse tree produced by WhileParser#stat.
    def visitStat(self, ctx: WhileParser.StatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by WhileParser#if_stat.
    def visitIf_stat(self, ctx: WhileParser.If_statContext):
        if self.visit(ctx.conditional).value:
            return self.visit(ctx.true)
        else:
            return self.visit(ctx.false)

    # Visit a parse tree produced by WhileParser#while_stat.
    def visitWhile_stat(self, ctx: WhileParser.While_statContext):
        if self.visit(ctx.conditional).value:
            return self.visit(ctx.inner)
        return


del WhileParser