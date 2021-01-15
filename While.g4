//While.g4

grammar While;

compileUnit
    :   expr EOF
    ;

expr
    : '(' expr ')' #PARENGRP
    | expr mulop expr #MULGRP
    | expr addop expr #ADDGRP
    | NUMBER #INT
    ;

addop: '+' | '-';
mulop: '*';

//asgn: ':=';
//SKP: 'skip';
//TRUE: 'true';
//FALSE: 'false';
//NOT: '¬';
//AND: '^';
//OR: 'v';
//LESS: '<';
//SEMI: ';';

NUMBER : ('0' .. '9') + ('.' ('0' .. '9') +)? ;
WS : [ \r\n\t] + -> skip ;