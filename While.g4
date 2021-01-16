//While.g4

grammar While;

compileUnit
    :   semi_stat EOF
    ;

semi_stat
    : stat (SEMI stat)*
    ;

stat
    : expr
    | if_stat
    | while_stat
    ;

expr
    : '(' expr ')' #PARENGRP
    | op=('+'|'-') expr   #UNARY
    | left=expr op='*' right=expr #INFIX
    | left=expr op=('+'|'-') right=expr #INFIX
    | left=expr op=('=' | '<') right=expr #INFIX
    | left=expr op=('∧' | '∨') right=expr #INFIX
    | op='¬' expr   #UNARYBOOL
    | left=expr op=':=' right=expr #INFIX
    | value=NUMBER #INT
    | value=(VAR|WORD_VAR) #VAL
    | value=(TRUE|FALSE) #BOOL
    | value=PASS #PASS
    ;

if_stat
    : IF conditional=expr THEN true=expr ELSE false=expr
    ;

while_stat
    : WHILE conditional=expr DO inner=stat
    | WHILE conditional=expr DO '{' inner=stat '}'
    ;

//////////////////////////////////
// LEXER
//////////////////////////////////
SEMI: ';';

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_ASGN: ':=';

OP_EQ: '=';
OP_NOT: '¬';
OP_AND: '∧';
OP_OR: '∨';
OP_LESS: '<';

TRUE: 'true';
FALSE: 'false';
IF: 'if';
THEN: 'then';
ELSE: 'else';
WHILE: 'while';
DO: 'do';

PASS: 'skip';
VAR : ('a'..'z');
WORD_VAR: ('A'..'Z')+;
NUMBER : [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?;
WS : [ \r\n\t] + -> skip ;