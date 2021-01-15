# Generated from While.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .WhileParser import WhileParser
else:
    from WhileParser import WhileParser

# This class defines a complete listener for a parse tree produced by WhileParser.
class WhileListener(ParseTreeListener):

    # Enter a parse tree produced by WhileParser#MULGRP.
    def enterMULGRP(self, ctx:WhileParser.MULGRPContext):
        pass

    # Exit a parse tree produced by WhileParser#MULGRP.
    def exitMULGRP(self, ctx:WhileParser.MULGRPContext):
        pass


    # Enter a parse tree produced by WhileParser#PARENGRP.
    def enterPARENGRP(self, ctx:WhileParser.PARENGRPContext):
        pass

    # Exit a parse tree produced by WhileParser#PARENGRP.
    def exitPARENGRP(self, ctx:WhileParser.PARENGRPContext):
        pass


    # Enter a parse tree produced by WhileParser#ADDGRP.
    def enterADDGRP(self, ctx:WhileParser.ADDGRPContext):
        pass

    # Exit a parse tree produced by WhileParser#ADDGRP.
    def exitADDGRP(self, ctx:WhileParser.ADDGRPContext):
        pass


    # Enter a parse tree produced by WhileParser#INT.
    def enterINT(self, ctx:WhileParser.INTContext):
        pass

    # Exit a parse tree produced by WhileParser#INT.
    def exitINT(self, ctx:WhileParser.INTContext):
        pass


    # Enter a parse tree produced by WhileParser#addop.
    def enterAddop(self, ctx:WhileParser.AddopContext):
        pass

    # Exit a parse tree produced by WhileParser#addop.
    def exitAddop(self, ctx:WhileParser.AddopContext):
        pass


    # Enter a parse tree produced by WhileParser#mulop.
    def enterMulop(self, ctx:WhileParser.MulopContext):
        pass

    # Exit a parse tree produced by WhileParser#mulop.
    def exitMulop(self, ctx:WhileParser.MulopContext):
        pass



del WhileParser