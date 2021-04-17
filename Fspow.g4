grammar Fspow;

prog:   stat+ ;

// labelling alternatives creates extra visitor methods
// the labels migh clash with rule names, so I make them unique

// I left it empty for you so you can be as creative as possible
stat;



ID: [a-zA-Z][a-zA-Z0-9]* ;
STRING: '"'.*?'"' 
    {self.text = self.text[1:-1]}
    ; //match anything in "..." but remove the quotes
WS : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> channel(HIDDEN);
INTEGER: [0-9]+ ;   // just non-negative ones for now
