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
    label (operator label)*
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

prints:
    'print ' ID
    |
    'print ' ID '[' label ']'
    |
    'print ' STRING
    ;

label:
    INTEGER
    |
    ID
    ;

loop:
    'for ' ID ' in range(' expression '):' stat*
    ;

length:
    ID '.length()'
    ;

ID: [a-zA-Z][a-zA-Z0-9]* ;
STRING: '"'.*?'"' 
    {self.text = self.text[1:-1]}
    ; //match anything in "..." but remove the quotes
WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> channel(HIDDEN);
INTEGER: [0-9]+ ;   // just non-negative ones for now
