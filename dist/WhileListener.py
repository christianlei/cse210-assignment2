# Generated from While.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser

# This class defines a complete listener for a parse tree produced by WhileParser.
class WhileListener(ParseTreeListener):

    # Enter a parse tree produced by WhileParser#compileUnit.
    def enterCompileUnit(self, ctx:WhileParser.CompileUnitContext):
        pass

    # Exit a parse tree produced by WhileParser#compileUnit.
    def exitCompileUnit(self, ctx:WhileParser.CompileUnitContext):
        pass


    # Enter a parse tree produced by WhileParser#INFIX.
    def enterINFIX(self, ctx:WhileParser.INFIXContext):
        pass

    # Exit a parse tree produced by WhileParser#INFIX.
    def exitINFIX(self, ctx:WhileParser.INFIXContext):
        pass


    # Enter a parse tree produced by WhileParser#PARENGRP.
    def enterPARENGRP(self, ctx:WhileParser.PARENGRPContext):
        pass

    # Exit a parse tree produced by WhileParser#PARENGRP.
    def exitPARENGRP(self, ctx:WhileParser.PARENGRPContext):
        pass


    # Enter a parse tree produced by WhileParser#UNARY.
    def enterUNARY(self, ctx:WhileParser.UNARYContext):
        pass

    # Exit a parse tree produced by WhileParser#UNARY.
    def exitUNARY(self, ctx:WhileParser.UNARYContext):
        pass


    # Enter a parse tree produced by WhileParser#INT.
    def enterINT(self, ctx:WhileParser.INTContext):
        pass

    # Exit a parse tree produced by WhileParser#INT.
    def exitINT(self, ctx:WhileParser.INTContext):
        pass



del WhileParser