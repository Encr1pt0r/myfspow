# Generated from Fspow.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FspowParser import FspowParser
else:
    from FspowParser import FspowParser

# This class defines a complete generic visitor for a parse tree produced by FspowParser.

class FspowVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FspowParser#prog.
    def visitProg(self, ctx:FspowParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statAssignment.
    def visitStatAssignment(self, ctx:FspowParser.StatAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statApplySelector.
    def visitStatApplySelector(self, ctx:FspowParser.StatApplySelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#print.
    def visitPrint(self, ctx:FspowParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statLoop.
    def visitStatLoop(self, ctx:FspowParser.StatLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#assignment.
    def visitAssignment(self, ctx:FspowParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#fcApplySelector.
    def visitFcApplySelector(self, ctx:FspowParser.FcApplySelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprID.
    def visitExprID(self, ctx:FspowParser.ExprIDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNewSelector.
    def visitExprNewSelector(self, ctx:FspowParser.ExprNewSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNewFileCollection.
    def visitExprNewFileCollection(self, ctx:FspowParser.ExprNewFileCollectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNumeric.
    def visitExprNumeric(self, ctx:FspowParser.ExprNumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprlength.
    def visitExprlength(self, ctx:FspowParser.ExprlengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#variable.
    def visitVariable(self, ctx:FspowParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#newSelector.
    def visitNewSelector(self, ctx:FspowParser.NewSelectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#selectorType.
    def visitSelectorType(self, ctx:FspowParser.SelectorTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#newFileCollection.
    def visitNewFileCollection(self, ctx:FspowParser.NewFileCollectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#rootSpecifier.
    def visitRootSpecifier(self, ctx:FspowParser.RootSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#numeric.
    def visitNumeric(self, ctx:FspowParser.NumericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#operator.
    def visitOperator(self, ctx:FspowParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#length.
    def visitLength(self, ctx:FspowParser.LengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#label.
    def visitLabel(self, ctx:FspowParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#prints.
    def visitPrints(self, ctx:FspowParser.PrintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#loop.
    def visitLoop(self, ctx:FspowParser.LoopContext):
        return self.visitChildren(ctx)



del FspowParser