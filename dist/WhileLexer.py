# Generated from While.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\n\6\n-\n\n\r\n\16\n.\3\n\3\n\6\n\63\n\n\r\n\16")
        buf.write("\n\64\5\n\67\n\n\3\n\3\n\5\n;\n\n\3\n\6\n>\n\n\r\n\16")
        buf.write("\n?\5\nB\n\n\3\13\6\13E\n\13\r\13\16\13F\3\13\3\13\2\2")
        buf.write("\f\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\3\2\6")
        buf.write("\3\2\62;\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\2P\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\3\27\3\2\2\2\5\31\3\2\2\2\7\33\3\2\2\2\t\35")
        buf.write("\3\2\2\2\13\37\3\2\2\2\r!\3\2\2\2\17$\3\2\2\2\21)\3\2")
        buf.write("\2\2\23,\3\2\2\2\25D\3\2\2\2\27\30\7*\2\2\30\4\3\2\2\2")
        buf.write("\31\32\7+\2\2\32\6\3\2\2\2\33\34\7-\2\2\34\b\3\2\2\2\35")
        buf.write("\36\7/\2\2\36\n\3\2\2\2\37 \7,\2\2 \f\3\2\2\2!\"\7<\2")
        buf.write("\2\"#\7?\2\2#\16\3\2\2\2$%\7u\2\2%&\7m\2\2&\'\7k\2\2\'")
        buf.write("(\7r\2\2(\20\3\2\2\2)*\4c|\2*\22\3\2\2\2+-\t\2\2\2,+\3")
        buf.write("\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\66\3\2\2\2\60\62")
        buf.write("\7\60\2\2\61\63\t\2\2\2\62\61\3\2\2\2\63\64\3\2\2\2\64")
        buf.write("\62\3\2\2\2\64\65\3\2\2\2\65\67\3\2\2\2\66\60\3\2\2\2")
        buf.write("\66\67\3\2\2\2\67A\3\2\2\28:\t\3\2\29;\t\4\2\2:9\3\2\2")
        buf.write("\2:;\3\2\2\2;=\3\2\2\2<>\t\2\2\2=<\3\2\2\2>?\3\2\2\2?")
        buf.write("=\3\2\2\2?@\3\2\2\2@B\3\2\2\2A8\3\2\2\2AB\3\2\2\2B\24")
        buf.write("\3\2\2\2CE\t\5\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2")
        buf.write("\2\2GH\3\2\2\2HI\b\13\2\2I\26\3\2\2\2\n\2.\64\66:?AF\3")
        buf.write("\b\2\2")
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
    PASS = 7
    VAR = 8
    NUMBER = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'+'", "'-'", "'*'", "':='" ]

    symbolicNames = [ "<INVALID>",
            "OP_ADD", "OP_SUB", "OP_MUL", "OP_ASGN", "PASS", "VAR", "NUMBER", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "OP_ADD", "OP_SUB", "OP_MUL", "OP_ASGN", 
                  "PASS", "VAR", "NUMBER", "WS" ]

    grammarFileName = "While.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


