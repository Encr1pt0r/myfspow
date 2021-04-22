grammar Fspow;

prog:   stat+ ;

stat:
    assignment  # statAssignment 
    |   
    fcApplySelector # statApplySelector
    |
    prints     # print
    |
    loop        # statLoop
    ;

assignment :
    ID '=' expression
    ;

fcApplySelector:
    ID '.apply(' expression ')'
    ;

expression : 
    variable              # exprID
    |
    newSelector     # exprNewSelector 
    |
    newFileCollection   # exprNewFileCollection
    |
    numeric         # exprNumeric
    |
    length           # exprlength
    ;

variable : ID;

newSelector :
    'Selector(' selectorType (',' selectorType)* ')'
    ;

selectorType :
    'name(' STRING ')'
    |
    'size(' STRING ')'
    ;

newFileCollection: 
    'FileCollection(' rootSpecifier ')'
    ;

rootSpecifier: 
    STRING
    ;
    
numeric : 
    label
    ;

operator:
    '+'
    |
    '-'
    |
    '*'
    |
    '/'
    ;

length:
    'len(' ID ')'
    ;

label:
    INTEGER
    |
    ID
    ;

prints:
    'print ' ID
    |
    'print ' ID '[' ID ']'
    |
    'print ' ID '[' INTEGER ']'
    |
    'print ' STRING
    |
    'print ' length
    ;

loop:
    'for ' ID ' in range(' length ') {' stat* '}'
    |
    'for ' ID ' in range(' INTEGER ') {' stat* '}'
    ;

ID: [a-zA-Z][a-zA-Z0-9]* ;
STRING: '"'.*?'"' 
    {self.text = self.text[1:-1]}
    ; //match anything in "..." but remove the quotes
WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> channel(HIDDEN);
INTEGER: [0-9]+ ;   // just non-negative ones for now
