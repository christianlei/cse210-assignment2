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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\64\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3")
        buf.write("\3\5\3\20\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4\35\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4(\n\4\f\4\16\4+\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\2\3\6\6\2\4\6\b\2\4\3\2\5\6\3\2\t\n\28\2\n\3\2\2\2\4")
        buf.write("\17\3\2\2\2\6\34\3\2\2\2\b,\3\2\2\2\n\13\5\4\3\2\13\f")
        buf.write("\7\2\2\3\f\3\3\2\2\2\r\20\5\6\4\2\16\20\5\b\5\2\17\r\3")
        buf.write("\2\2\2\17\16\3\2\2\2\20\5\3\2\2\2\21\22\b\4\1\2\22\23")
        buf.write("\7\3\2\2\23\24\5\6\4\2\24\25\7\4\2\2\25\35\3\2\2\2\26")
        buf.write("\27\t\2\2\2\27\35\5\6\4\n\30\35\7\20\2\2\31\35\7\17\2")
        buf.write("\2\32\35\t\3\2\2\33\35\7\16\2\2\34\21\3\2\2\2\34\26\3")
        buf.write("\2\2\2\34\30\3\2\2\2\34\31\3\2\2\2\34\32\3\2\2\2\34\33")
        buf.write("\3\2\2\2\35)\3\2\2\2\36\37\f\t\2\2\37 \7\b\2\2 (\5\6\4")
        buf.write("\n!\"\f\b\2\2\"#\7\7\2\2#(\5\6\4\t$%\f\7\2\2%&\t\2\2\2")
        buf.write("&(\5\6\4\b\'\36\3\2\2\2\'!\3\2\2\2\'$\3\2\2\2(+\3\2\2")
        buf.write("\2)\'\3\2\2\2)*\3\2\2\2*\7\3\2\2\2+)\3\2\2\2,-\7\13\2")
        buf.write("\2-.\5\6\4\2./\7\f\2\2/\60\5\6\4\2\60\61\7\r\2\2\61\62")
        buf.write("\5\6\4\2\62\t\3\2\2\2\6\17\34\')")
        return buf.getvalue()


class WhileParser ( Parser ):

    grammarFileName = "While.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "':='", 
                     "'true'", "'false'", "'if'", "'then'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OP_ADD", "OP_SUB", 
                      "OP_MUL", "OP_ASGN", "TRUE", "FALSE", "IF", "THEN", 
                      "ELSE", "PASS", "VAR", "NUMBER", "WS" ]

    RULE_compileUnit = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_if_stat = 3

    ruleNames =  [ "compileUnit", "stat", "expr", "if_stat" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OP_ADD=3
    OP_SUB=4
    OP_MUL=5
    OP_ASGN=6
    TRUE=7
    FALSE=8
    IF=9
    THEN=10
    ELSE=11
    PASS=12
    VAR=13
    NUMBER=14
    WS=15

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

        def stat(self):
            return self.getTypedRuleContext(WhileParser.StatContext,0)


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
            self.state = 8
            self.stat()
            self.state = 9
            self.match(WhileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(WhileParser.ExprContext,0)


        def if_stat(self):
            return self.getTypedRuleContext(WhileParser.If_statContext,0)


        def getRuleIndex(self):
            return WhileParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = WhileParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.T__0, WhileParser.OP_ADD, WhileParser.OP_SUB, WhileParser.TRUE, WhileParser.FALSE, WhileParser.PASS, WhileParser.VAR, WhileParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                pass
            elif token in [WhileParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 12
                self.if_stat()
                pass
            else:
                raise NoViableAltException(self)

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


    class VALContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(WhileParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVAL" ):
                listener.enterVAL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVAL" ):
                listener.exitVAL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVAL" ):
                return visitor.visitVAL(self)
            else:
                return visitor.visitChildren(self)


    class PASSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def PASS(self):
            return self.getToken(WhileParser.PASS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPASS" ):
                listener.enterPASS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPASS" ):
                listener.exitPASS(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPASS" ):
                return visitor.visitPASS(self)
            else:
                return visitor.visitChildren(self)


    class BOOLContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileParser.ExprContext
            super().__init__(parser)
            self.value = None # Token
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(WhileParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(WhileParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBOOL" ):
                listener.enterBOOL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBOOL" ):
                listener.exitBOOL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBOOL" ):
                return visitor.visitBOOL(self)
            else:
                return visitor.visitChildren(self)


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

        def OP_ASGN(self):
            return self.getToken(WhileParser.OP_ASGN, 0)
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileParser.T__0]:
                localctx = WhileParser.PARENGRPContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 16
                self.match(WhileParser.T__0)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(WhileParser.T__1)
                pass
            elif token in [WhileParser.OP_ADD, WhileParser.OP_SUB]:
                localctx = WhileParser.UNARYContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==WhileParser.OP_ADD or _la==WhileParser.OP_SUB):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.expr(8)
                pass
            elif token in [WhileParser.NUMBER]:
                localctx = WhileParser.INTContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                localctx.value = self.match(WhileParser.NUMBER)
                pass
            elif token in [WhileParser.VAR]:
                localctx = WhileParser.VALContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                localctx.value = self.match(WhileParser.VAR)
                pass
            elif token in [WhileParser.TRUE, WhileParser.FALSE]:
                localctx = WhileParser.BOOLContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                localctx.value = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==WhileParser.TRUE or _la==WhileParser.FALSE):
                    localctx.value = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [WhileParser.PASS]:
                localctx = WhileParser.PASSContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                localctx.value = self.match(WhileParser.PASS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 29
                        localctx.op = self.match(WhileParser.OP_ASGN)
                        self.state = 30
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 32
                        localctx.op = self.match(WhileParser.OP_MUL)
                        self.state = 33
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = WhileParser.INFIXContext(self, WhileParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 35
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileParser.OP_ADD or _la==WhileParser.OP_SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 36
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.conditional = None # ExprContext
            self.true = None # ExprContext
            self.false = None # ExprContext

        def IF(self):
            return self.getToken(WhileParser.IF, 0)

        def THEN(self):
            return self.getToken(WhileParser.THEN, 0)

        def ELSE(self):
            return self.getToken(WhileParser.ELSE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileParser.ExprContext,i)


        def getRuleIndex(self):
            return WhileParser.RULE_if_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stat" ):
                listener.enterIf_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stat" ):
                listener.exitIf_stat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stat" ):
                return visitor.visitIf_stat(self)
            else:
                return visitor.visitChildren(self)




    def if_stat(self):

        localctx = WhileParser.If_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_if_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(WhileParser.IF)
            self.state = 43
            localctx.conditional = self.expr(0)
            self.state = 44
            self.match(WhileParser.THEN)
            self.state = 45
            localctx.true = self.expr(0)
            self.state = 46
            self.match(WhileParser.ELSE)
            self.state = 47
            localctx.false = self.expr(0)
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
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




