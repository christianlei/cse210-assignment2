//While.g4

grammar While;

compileUnit
    :   expr EOF
    ;

expr
    : '(' expr ')' #PARENGRP
    | op=('+'|'-') expr   #UNARY
    | left=expr op=':=' right=expr #INFIX
    | left=expr op='*' right=expr #INFIX
    | left=expr op=('+'|'-') right=expr #INFIX
    | value=NUMBER #INT
    | value=VAR #VAL
    | value=(TRUE|FALSE) #BOOL
    | value=PASS #PASS
    ;

if_stat
    : IF TRUE THEN expr ELSE expr
    ;


OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_ASGN: ':=';

TRUE: 'true';
FALSE: 'false';
IF: 'if';
THEN: 'then';
ELSE: 'else';
//NOT: '¬';
//AND: '^';
//OR: 'v';
//LESS: '<';
//SEMI: ';';

PASS: ('skip');
VAR : ('a'..'z');
NUMBER : [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?;
WS : [ \r\n\t] + -> skip ;