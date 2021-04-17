# Generated from Fspow.g4 by ANTLR 4.9.1
from antlr4 import *
from idlelib.idle_test.test_configdialog import root
if __name__ is not None and "." in __name__:
    from .FspowParser import FspowParser
else:
    from FspowParser import FspowParser

# superclass
from FspowVisitor import FspowVisitor

# our own imports:
from repertoire.FileCollection import *
from repertoire.Selector import *
from repertoire.FSObject import *
from repertoire.FileCollectionIterator import *

# for symbol table
from collections import defaultdict


# This class defines a complete specific visitor for a parse tree produced by FspowParser.

class FspowVisitorUser(FspowVisitor):
    
    # where all the variables reside
    variablesTable = defaultdict()
    
    def retrieveVariable(self, identifier):
        """
        retrieve value of item in variablesTable identified using identifier or complain and return None
        """
        if identifier in self.variablesTable:
            return self.variablesTable[identifier]
        else:
            print("Error: identifier", identifier, "not found")
            return None
        
del FspowParser
