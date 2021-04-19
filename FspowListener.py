# Generated from Fspow.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FspowParser import FspowParser
else:
    from FspowParser import FspowParser

# This class defines a complete listener for a parse tree produced by FspowParser.
class FspowListener(ParseTreeListener):

    # Enter a parse tree produced by FspowParser#prog.
    def enterProg(self, ctx:FspowParser.ProgContext):
        pass

    # Exit a parse tree produced by FspowParser#prog.
    def exitProg(self, ctx:FspowParser.ProgContext):
        pass


    # Enter a parse tree produced by FspowParser#statAssignment.
    def enterStatAssignment(self, ctx:FspowParser.StatAssignmentContext):
        pass

    # Exit a parse tree produced by FspowParser#statAssignment.
    def exitStatAssignment(self, ctx:FspowParser.StatAssignmentContext):
        pass


    # Enter a parse tree produced by FspowParser#statApplySelector.
    def enterStatApplySelector(self, ctx:FspowParser.StatApplySelectorContext):
        pass

    # Exit a parse tree produced by FspowParser#statApplySelector.
    def exitStatApplySelector(self, ctx:FspowParser.StatApplySelectorContext):
        pass


    # Enter a parse tree produced by FspowParser#print.
    def enterPrint(self, ctx:FspowParser.PrintContext):
        pass

    # Exit a parse tree produced by FspowParser#print.
    def exitPrint(self, ctx:FspowParser.PrintContext):
        pass


    # Enter a parse tree produced by FspowParser#statLoop.
    def enterStatLoop(self, ctx:FspowParser.StatLoopContext):
        pass

    # Exit a parse tree produced by FspowParser#statLoop.
    def exitStatLoop(self, ctx:FspowParser.StatLoopContext):
        pass


    # Enter a parse tree produced by FspowParser#assignment.
    def enterAssignment(self, ctx:FspowParser.AssignmentContext):
        pass

    # Exit a parse tree produced by FspowParser#assignment.
    def exitAssignment(self, ctx:FspowParser.AssignmentContext):
        pass


    # Enter a parse tree produced by FspowParser#fcApplySelector.
    def enterFcApplySelector(self, ctx:FspowParser.FcApplySelectorContext):
        pass

    # Exit a parse tree produced by FspowParser#fcApplySelector.
    def exitFcApplySelector(self, ctx:FspowParser.FcApplySelectorContext):
        pass


    # Enter a parse tree produced by FspowParser#exprID.
    def enterExprID(self, ctx:FspowParser.ExprIDContext):
        pass

    # Exit a parse tree produced by FspowParser#exprID.
    def exitExprID(self, ctx:FspowParser.ExprIDContext):
        pass


    # Enter a parse tree produced by FspowParser#exprNewSelector.
    def enterExprNewSelector(self, ctx:FspowParser.ExprNewSelectorContext):
        pass

    # Exit a parse tree produced by FspowParser#exprNewSelector.
    def exitExprNewSelector(self, ctx:FspowParser.ExprNewSelectorContext):
        pass


    # Enter a parse tree produced by FspowParser#exprNewFileCollection.
    def enterExprNewFileCollection(self, ctx:FspowParser.ExprNewFileCollectionContext):
        pass

    # Exit a parse tree produced by FspowParser#exprNewFileCollection.
    def exitExprNewFileCollection(self, ctx:FspowParser.ExprNewFileCollectionContext):
        pass


    # Enter a parse tree produced by FspowParser#exprNumeric.
    def enterExprNumeric(self, ctx:FspowParser.ExprNumericContext):
        pass

    # Exit a parse tree produced by FspowParser#exprNumeric.
    def exitExprNumeric(self, ctx:FspowParser.ExprNumericContext):
        pass


    # Enter a parse tree produced by FspowParser#exprlength.
    def enterExprlength(self, ctx:FspowParser.ExprlengthContext):
        pass

    # Exit a parse tree produced by FspowParser#exprlength.
    def exitExprlength(self, ctx:FspowParser.ExprlengthContext):
        pass


    # Enter a parse tree produced by FspowParser#variable.
    def enterVariable(self, ctx:FspowParser.VariableContext):
        pass

    # Exit a parse tree produced by FspowParser#variable.
    def exitVariable(self, ctx:FspowParser.VariableContext):
        pass


    # Enter a parse tree produced by FspowParser#newSelector.
    def enterNewSelector(self, ctx:FspowParser.NewSelectorContext):
        pass

    # Exit a parse tree produced by FspowParser#newSelector.
    def exitNewSelector(self, ctx:FspowParser.NewSelectorContext):
        pass


    # Enter a parse tree produced by FspowParser#selectorType.
    def enterSelectorType(self, ctx:FspowParser.SelectorTypeContext):
        pass

    # Exit a parse tree produced by FspowParser#selectorType.
    def exitSelectorType(self, ctx:FspowParser.SelectorTypeContext):
        pass


    # Enter a parse tree produced by FspowParser#newFileCollection.
    def enterNewFileCollection(self, ctx:FspowParser.NewFileCollectionContext):
        pass

    # Exit a parse tree produced by FspowParser#newFileCollection.
    def exitNewFileCollection(self, ctx:FspowParser.NewFileCollectionContext):
        pass


    # Enter a parse tree produced by FspowParser#rootSpecifier.
    def enterRootSpecifier(self, ctx:FspowParser.RootSpecifierContext):
        pass

    # Exit a parse tree produced by FspowParser#rootSpecifier.
    def exitRootSpecifier(self, ctx:FspowParser.RootSpecifierContext):
        pass


    # Enter a parse tree produced by FspowParser#numeric.
    def enterNumeric(self, ctx:FspowParser.NumericContext):
        pass

    # Exit a parse tree produced by FspowParser#numeric.
    def exitNumeric(self, ctx:FspowParser.NumericContext):
        pass


    # Enter a parse tree produced by FspowParser#operator.
    def enterOperator(self, ctx:FspowParser.OperatorContext):
        pass

    # Exit a parse tree produced by FspowParser#operator.
    def exitOperator(self, ctx:FspowParser.OperatorContext):
        pass


    # Enter a parse tree produced by FspowParser#prints.
    def enterPrints(self, ctx:FspowParser.PrintsContext):
        pass

    # Exit a parse tree produced by FspowParser#prints.
    def exitPrints(self, ctx:FspowParser.PrintsContext):
        pass


    # Enter a parse tree produced by FspowParser#label.
    def enterLabel(self, ctx:FspowParser.LabelContext):
        pass

    # Exit a parse tree produced by FspowParser#label.
    def exitLabel(self, ctx:FspowParser.LabelContext):
        pass


    # Enter a parse tree produced by FspowParser#loop.
    def enterLoop(self, ctx:FspowParser.LoopContext):
        pass

    # Exit a parse tree produced by FspowParser#loop.
    def exitLoop(self, ctx:FspowParser.LoopContext):
        pass


    # Enter a parse tree produced by FspowParser#length.
    def enterLength(self, ctx:FspowParser.LengthContext):
        pass

    # Exit a parse tree produced by FspowParser#length.
    def exitLength(self, ctx:FspowParser.LengthContext):
        pass



del FspowParser