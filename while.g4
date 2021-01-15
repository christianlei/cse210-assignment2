//While.g4

grammar While;

//Token

expr : '-' expr #UMINUS
    | expr mulop expr #MULGRP
    | expr addop expr #ADDGRP
    | '(' expr ')' #PARENGRP
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