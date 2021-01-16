# Generated from While.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("l\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\17")
        buf.write("\6\17O\n\17\r\17\16\17P\3\17\3\17\6\17U\n\17\r\17\16\17")
        buf.write("V\5\17Y\n\17\3\17\3\17\5\17]\n\17\3\17\6\17`\n\17\r\17")
        buf.write("\16\17a\5\17d\n\17\3\20\6\20g\n\20\r\20\16\20h\3\20\3")
        buf.write("\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21\3\2\6\3\2\62;\4\2GGgg")
        buf.write("\4\2--//\5\2\13\f\17\17\"\"\2r\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3\2\2\2\13)")
        buf.write("\3\2\2\2\r+\3\2\2\2\17.\3\2\2\2\21\63\3\2\2\2\239\3\2")
        buf.write("\2\2\25<\3\2\2\2\27A\3\2\2\2\31F\3\2\2\2\33K\3\2\2\2\35")
        buf.write("N\3\2\2\2\37f\3\2\2\2!\"\7*\2\2\"\4\3\2\2\2#$\7+\2\2$")
        buf.write("\6\3\2\2\2%&\7-\2\2&\b\3\2\2\2\'(\7/\2\2(\n\3\2\2\2)*")
        buf.write("\7,\2\2*\f\3\2\2\2+,\7<\2\2,-\7?\2\2-\16\3\2\2\2./\7v")
        buf.write("\2\2/\60\7t\2\2\60\61\7w\2\2\61\62\7g\2\2\62\20\3\2\2")
        buf.write("\2\63\64\7h\2\2\64\65\7c\2\2\65\66\7n\2\2\66\67\7u\2\2")
        buf.write("\678\7g\2\28\22\3\2\2\29:\7k\2\2:;\7h\2\2;\24\3\2\2\2")
        buf.write("<=\7v\2\2=>\7j\2\2>?\7g\2\2?@\7p\2\2@\26\3\2\2\2AB\7g")
        buf.write("\2\2BC\7n\2\2CD\7u\2\2DE\7g\2\2E\30\3\2\2\2FG\7u\2\2G")
        buf.write("H\7m\2\2HI\7k\2\2IJ\7r\2\2J\32\3\2\2\2KL\4c|\2L\34\3\2")
        buf.write("\2\2MO\t\2\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2")
        buf.write("QX\3\2\2\2RT\7\60\2\2SU\t\2\2\2TS\3\2\2\2UV\3\2\2\2VT")
        buf.write("\3\2\2\2VW\3\2\2\2WY\3\2\2\2XR\3\2\2\2XY\3\2\2\2Yc\3\2")
        buf.write("\2\2Z\\\t\3\2\2[]\t\4\2\2\\[\3\2\2\2\\]\3\2\2\2]_\3\2")
        buf.write("\2\2^`\t\2\2\2_^\3\2\2\2`a\3\2\2\2a_\3\2\2\2ab\3\2\2\2")
        buf.write("bd\3\2\2\2cZ\3\2\2\2cd\3\2\2\2d\36\3\2\2\2eg\t\5\2\2f")
        buf.write("e\3\2\2\2gh\3\2\2\2hf\3\2\2\2hi\3\2\2\2ij\3\2\2\2jk\b")
        buf.write("\20\2\2k \3\2\2\2\n\2PVX\\ach\3\b\2\2")
        return buf.getvalue()


class WhileLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    OP_ADD = 3
    OP_SUB = 4
    OP_MUL = 5
    OP_ASGN = 6
    TRUE = 7
    FALSE = 8
    IF = 9
    THEN = 10
    ELSE = 11
    PASS = 12
    VAR = 13
    NUMBER = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "':='", "'true'", "'false'", 
            "'if'", "'then'", "'else'" ]

    symbolicNames = [ "<INVALID>",
            "OP_ADD", "OP_SUB", "OP_MUL", "OP_ASGN", "TRUE", "FALSE", "IF", 
            "THEN", "ELSE", "PASS", "VAR", "NUMBER", "WS" ]

    ruleNames = [ "T__0", "T__1", "OP_ADD", "OP_SUB", "OP_MUL", "OP_ASGN", 
                  "TRUE", "FALSE", "IF", "THEN", "ELSE", "PASS", "VAR", 
                  "NUMBER", "WS" ]

    grammarFileName = "While.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


