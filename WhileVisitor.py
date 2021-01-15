# Generated from While.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser

# This class defines a complete generic visitor for a parse tree produced by WhileParser.

class WhileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileParser#MULGRP.
    def visitMULGRP(self, ctx:WhileParser.MULGRPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#PARENGRP.
    def visitPARENGRP(self, ctx:WhileParser.PARENGRPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#ADDGRP.
    def visitADDGRP(self, ctx:WhileParser.ADDGRPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#INT.
    def visitINT(self, ctx:WhileParser.INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#addop.
    def visitAddop(self, ctx:WhileParser.AddopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileParser#mulop.
    def visitMulop(self, ctx:WhileParser.MulopContext):
        return self.visitChildren(ctx)



del WhileParser