//While.g4

grammar While;

compileUnit
    :   expr EOF
    ;

expr
    : '(' expr ')' #PARENGRP
    | op=('+'|'-') expr   #UNARY
    |
    | left=expr op='*' right=expr #INFIX
    | left=expr op=('+'|'-') right=expr #INFIX
    | value=NUMBER #INT
    ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_ASGN: ':=';
//SKP: 'skip';
//TRUE: 'true';
//FALSE: 'false';
//NOT: '¬';
//AND: '^';
//OR: 'v';
//LESS: '<';
//SEMI: ';';

VAR : [a-z];
NUMBER : [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?;
WS : [ \r\n\t] + -> skip ;