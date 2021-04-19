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
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statAssignment.
    def visitStatAssignment(self, ctx:FspowParser.StatAssignmentContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statApplySelector.
    def visitStatApplySelector(self, ctx:FspowParser.StatApplySelectorContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#print.
    def visitPrint(self, ctx:FspowParser.PrintContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statLoop.
    def visitStatLoop(self, ctx:FspowParser.StatLoopContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#assignment.
    def visitAssignment(self, ctx:FspowParser.AssignmentContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#fcApplySelector.
    def visitFcApplySelector(self, ctx:FspowParser.FcApplySelectorContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprID.
    def visitExprID(self, ctx:FspowParser.ExprIDContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNewSelector.
    def visitExprNewSelector(self, ctx:FspowParser.ExprNewSelectorContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNewFileCollection.
    def visitExprNewFileCollection(self, ctx:FspowParser.ExprNewFileCollectionContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNumeric.
    def visitExprNumeric(self, ctx:FspowParser.ExprNumericContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprlength.
    def visitExprlength(self, ctx:FspowParser.ExprlengthContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#variable.
    def visitVariable(self, ctx:FspowParser.VariableContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#newSelector.
    def visitNewSelector(self, ctx:FspowParser.NewSelectorContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#selectorType.
    def visitSelectorType(self, ctx:FspowParser.SelectorTypeContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#newFileCollection.
    def visitNewFileCollection(self, ctx:FspowParser.NewFileCollectionContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#rootSpecifier.
    def visitRootSpecifier(self, ctx:FspowParser.RootSpecifierContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#numeric.
    def visitNumeric(self, ctx:FspowParser.NumericContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#operator.
    def visitOperator(self, ctx:FspowParser.OperatorContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#prints.
    def visitPrints(self, ctx:FspowParser.PrintsContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#loop.
    def visitLoop(self, ctx:FspowParser.LoopContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#length.
    def visitLength(self, ctx:FspowParser.LengthContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FspowParser#label.
    def visitLabel(self, ctx:FspowParser.LabelContext):
        for i in range(ctx.getChildCount()):
            print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)
        
del FspowParser
