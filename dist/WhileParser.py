# Generated from While.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\37\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\22\n\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\32\n")
        buf.write("\3\f\3\16\3\35\13\3\3\3\2\3\4\4\2\4\2\3\3\2\5\6\2 \2\6")
        buf.write("\3\2\2\2\4\21\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2")
        buf.write("\2\2\t\n\b\3\1\2\n\13\7\3\2\2\13\f\5\4\3\2\f\r\7\4\2\2")
        buf.write("\r\22\3\2\2\2\16\17\t\2\2\2\17\22\5\4\3\6\20\22\7\b\2")
        buf.write("\2\21\t\3\2\2\2\21\16\3\2\2\2\21\20\3\2\2\2\22\33\3\2")
        buf.write("\2\2\23\24\f\5\2\2\24\25\7\7\2\2\25\32\5\4\3\6\26\27\f")
        buf.write("\4\2\2\27\30\t\2\2\2\30\32\5\4\3\5\31\23\3\2\2\2\31\26")
        buf.write("\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\5\3\2\2\2\35\33\3\2\2\2\5\21\31\33")
        return buf.getvalue()


class WhileParser ( Parser ):

    grammarFileName = "While.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OP_ADD", "OP_SUB", 
                      "OP_MUL", "NUMBER", "WS" ]

    RULE_compileUnit = 0
    RULE_expr = 1

    ruleNames =  [ "compileUnit", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OP_ADD=3
    OP_SUB=4
    OP_MUL=5
    NUMBER=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CompileUnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)


        def EOF(self):
            return self.getToken(WhileParser.EOF, 0)

        def getRuleIndex(self):
            return WhileParser.RULE_compileUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompileUnit" ):
                listener.enterCompileUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompileUnit" ):
                listener.exitCompileUnit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompileUnit" ):
                return visitor.visitCompileUnit(self)
            else:
                return visitor.visitChildren(self)




    def compileUnit(self):

        localctx = WhileParser.CompileUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compileUnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(WhileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class INFIXContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)

        def OP_MUL(self):
            return self.getToken(WhileParser.OP_MUL, 0)
        def OP_ADD(self):
            return self.getToken(WhileParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(WhileParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterINFIX" ):
                listener.enterINFIX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitINFIX" ):
                listener.exitINFIX(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINFIX" ):
                return visitor.visitINFIX(self)
            else:
                return visitor.visitChildren(self)


    class PARENGRPContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPARENGRP" ):
                listener.enterPARENGRP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPARENGRP" ):
                listener.exitPARENGRP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPARENGRP" ):
                return visitor.visitPARENGRP(self)
            else:
                return visitor.visitChildren(self)


    class UNARYContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)

        def OP_ADD(self):
            return self.getToken(WhileParser.OP_ADD, 0)
        def OP_SUB(self):
            return self.getToken(WhileParser.OP_SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUNARY" ):
                listener.enterUNARY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUNARY" ):
                listener.exitUNARY(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUNARY" ):
                return visitor.visitUNARY(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(WhileParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterINT" ):
                listener.enterINT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitINT" ):
                listener.exitINT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.T__0]:
                localctx = WhileParser.PARENGRPContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 8
                self.match(WhileParser.T__0)
                self.state = 9
                self.expr(0)
                self.state = 10
                self.match(WhileParser.T__1)
                pass
            elif token in [WhileParser.OP_ADD, WhileParser.OP_SUB]:
                localctx = WhileParser.UNARYContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==WhileParser.OP_ADD or _la==WhileParser.OP_SUB):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 13
                self.expr(4)
                pass
            elif token in [WhileParser.NUMBER]:
                localctx = WhileParser.INTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 14
                localctx.value = self.match(WhileParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 25
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 23
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 17
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 18
                        localctx.op = self.match(WhileParser.OP_MUL)
                        self.state = 19
                        localctx.right = self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 20
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 21
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileParser.OP_ADD or _la==WhileParser.OP_SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 22
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 27
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




