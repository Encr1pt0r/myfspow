# main.py
"""
Test fspow parser
"""

import sys

from antlr4 import *
from FspowLexer import FspowLexer
from FspowParser import FspowParser
from FspowListener import FspowListener
# from antlr4.tree.Trees import Trees
from TreesUser import TreesUser


def main(argv):
    # argv[1] s/be name of source file
    # if missing, use stdin
    if len(argv) == 1:
        # StdinStream is a standard ANTLR class read by the lexer
        # (It is not a file descriptor)        
        inpstream = StdinStream()
    else:
        inpname = argv[1]
        # FileStream is a standard ANTLR class read by the lexer
        # (It is not a file descriptor)        
        inpstream = FileStream(inpname)

    

    # The lexer analyses the characters on inpstream and produces tokens 
    lexer = FspowLexer(inpstream)
    # .. on the token stream (belonging to a standard ANTLR class)
    tokstream = CommonTokenStream(lexer)

    # The parser produces an abstract syntax tree
    parser = FspowParser(tokstream)
    # When we execute the parse, we need to give it the starting rule of our grammar,
    # which in our case is 'start' (as defined in Fspow.g4),
    # so here we invoke the method named after this rule: start()
    tree = parser.prog()

    # print the parse tree
    print(TreesUser.toStringTree(tree, None, parser))
    print(TreesUser.PrettyPrint(tree, None, parser))
    
    # The listener defines the actions to take upon entering an exiting nodes for 
    # specific tokens on the AST
    # listener = FspowListener()
    
    # A ParseTreeWalker is annother standard ANTLR class, that performs a walk on the AST
    # walker = ParseTreeWalker()

    # Get the tree walker to perform a walk on the AST, getting the listener to perform
    # the appropriate actions
    # walker.walk~(listener, tree)




if __name__ == '__main__':
    main(sys.argv)
