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

        # Visit a parse tree produced by FspowParser#prog.
    def visitProg(self, ctx:FspowParser.ProgContext):
        """
        One child: the stat line
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statAssignment.
    def visitStatAssignment(self, ctx:FspowParser.StatAssignmentContext):
        """
        One child: Assignment command (x = 5)
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statApplySelector.
    def visitStatApplySelector(self, ctx:FspowParser.StatApplySelectorContext):
        """
        One child: wombats.apply(Selector())
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#print.
    def visitPrint(self, ctx:FspowParser.PrintContext):
        """
        one child   :   print statement
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statLoop.
    def visitStatLoop(self, ctx:FspowParser.StatLoopContext):
        """
        One child: for ID in range( expression ):
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#assignment.
    def visitAssignment(self, ctx:FspowParser.AssignmentContext):
        """
        Minimum 3 chidren:
            0   :   variable
            1   :   '='
            2   :   label (INTEGER or ID), FileCollection()
            +   :   Chilren 1 and 2 again
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#fcApplySelector.
    def visitFcApplySelector(self, ctx:FspowParser.FcApplySelectorContext):
        """
        Children:
            0   :   ID
            1   :   '.apply('
            2   :   expression
            3   :   ')'
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprID.
    def visitExprID(self, ctx:FspowParser.ExprIDContext):
        """
        One child: ID
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNewSelector.
    def visitExprNewSelector(self, ctx:FspowParser.ExprNewSelectorContext):
        """
        One child: new Selector statment
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNewFileCollection.
    def visitExprNewFileCollection(self, ctx:FspowParser.ExprNewFileCollectionContext):
        """
        3 children:
            0   :   'FileCollection'
            1   :   ID
            2   :   ')'
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNumeric.
    def visitExprNumeric(self, ctx:FspowParser.ExprNumericContext):
        """
        One child   :   assignment with out the '='
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprlength.
    def visitExprlength(self, ctx:FspowParser.ExprlengthContext):
        """
        One child: 'ID.length()'
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#variable.
    def visitVariable(self, ctx:FspowParser.VariableContext):
        """
        One child: ID
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#newSelector.
    def visitNewSelector(self, ctx:FspowParser.NewSelectorContext):
        """
        Children:
            0   :   'Selector('
            1   :   selectorType
            2+  :   ','
            3+  :   selectorType*
            2   :   ')'
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#selectorType.
    def visitSelectorType(self, ctx:FspowParser.SelectorTypeContext):
        """
        Children:
            0   :   'name('
            1   :   STRING
            2   :   ')'
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#newFileCollection.
    def visitNewFileCollection(self, ctx:FspowParser.NewFileCollectionContext):
        """
        Children:
            0   :   'FileCollection('
            1   :   ID
            2   :   ')'
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#rootSpecifier.
    def visitRootSpecifier(self, ctx:FspowParser.RootSpecifierContext):
        """
        One child   :   ID
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#numeric.
    def visitNumeric(self, ctx:FspowParser.NumericContext):
        """
        Minimum children 1:
            0   :   label (INTEGER or ID)
            +   :   operator
            +   :   label 
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#operator.
    def visitOperator(self, ctx:FspowParser.OperatorContext):
        """
        One child   :   operator ('+', '-', '*', '/')
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#prints.
    def visitPrints(self, ctx:FspowParser.PrintsContext):
        """
        Type A: print "message"
            0   :   'print'
            1   :   STRING

        Type B: print wombats
            0   :   'print'
            1   :   ID

        Type C: print womabats[x]
            0   :   'print'
            1   :   '['
            2   :   label (INTEGER or ID)
            3   :   ']'
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#loop.
    def visitLoop(self, ctx:FspowParser.LoopContext):
        """
        Children:
            0   :   'for'
            1   :   ID
            2   :   ' in range('
            3   :   ID
            4   :   '):'
            5   :   stat*
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#length.
    def visitLength(self, ctx:FspowParser.LengthContext):
        """
        Children:
            0   :   ID
            1   :   '.length()'
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FspowParser#label.
    def visitLabel(self, ctx:FspowParser.LabelContext):
        """
        One child   :   label (INTEGER or ID)
        """
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)
        
del FspowParser
