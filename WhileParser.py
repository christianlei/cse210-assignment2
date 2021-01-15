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
        buf.write("\"\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\5\2")
        buf.write("\17\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\7\2\31\n\2\f\2")
        buf.write("\16\2\34\13\2\3\3\3\3\3\4\3\4\3\4\2\3\2\5\2\4\6\2\3\3")
        buf.write("\2\5\6\2!\2\16\3\2\2\2\4\35\3\2\2\2\6\37\3\2\2\2\b\t\b")
        buf.write("\2\1\2\t\n\7\3\2\2\n\13\5\2\2\2\13\f\7\4\2\2\f\17\3\2")
        buf.write("\2\2\r\17\7\b\2\2\16\b\3\2\2\2\16\r\3\2\2\2\17\32\3\2")
        buf.write("\2\2\20\21\f\5\2\2\21\22\5\6\4\2\22\23\5\2\2\6\23\31\3")
        buf.write("\2\2\2\24\25\f\4\2\2\25\26\5\4\3\2\26\27\5\2\2\5\27\31")
        buf.write("\3\2\2\2\30\20\3\2\2\2\30\24\3\2\2\2\31\34\3\2\2\2\32")
        buf.write("\30\3\2\2\2\32\33\3\2\2\2\33\3\3\2\2\2\34\32\3\2\2\2\35")
        buf.write("\36\t\2\2\2\36\5\3\2\2\2\37 \7\7\2\2 \7\3\2\2\2\5\16\30")
        buf.write("\32")
        return buf.getvalue()


class WhileParser ( Parser ):

    grammarFileName = "While.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_expr = 0
    RULE_addop = 1
    RULE_mulop = 2

    ruleNames =  [ "expr", "addop", "mulop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MULGRPContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)

        def mulop(self):
            return self.getTypedRuleContext(WhileParser.MulopContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMULGRP" ):
                listener.enterMULGRP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMULGRP" ):
                listener.exitMULGRP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMULGRP" ):
                return visitor.visitMULGRP(self)
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


    class ADDGRPContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)

        def addop(self):
            return self.getTypedRuleContext(WhileParser.AddopContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterADDGRP" ):
                listener.enterADDGRP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitADDGRP" ):
                listener.exitADDGRP(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitADDGRP" ):
                return visitor.visitADDGRP(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
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
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.T__0]:
                localctx = WhileParser.PARENGRPContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(WhileParser.T__0)
                self.state = 8
                self.expr(0)
                self.state = 9
                self.match(WhileParser.T__1)
                pass
            elif token in [WhileParser.NUMBER]:
                localctx = WhileParser.INTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(WhileParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = WhileParser.MULGRPContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 14
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 15
                        self.mulop()
                        self.state = 16
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = WhileParser.ADDGRPContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 19
                        self.addop()
                        self.state = 20
                        self.expr(3)
                        pass

             
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AddopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_addop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddop" ):
                listener.enterAddop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddop" ):
                listener.exitAddop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddop" ):
                return visitor.visitAddop(self)
            else:
                return visitor.visitChildren(self)




    def addop(self):

        localctx = WhileParser.AddopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_addop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not(_la==WhileParser.T__2 or _la==WhileParser.T__3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileParser.RULE_mulop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulop" ):
                listener.enterMulop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulop" ):
                listener.exitMulop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulop" ):
                return visitor.visitMulop(self)
            else:
                return visitor.visitChildren(self)




    def mulop(self):

        localctx = WhileParser.MulopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mulop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(WhileParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
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
         




