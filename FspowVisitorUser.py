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
            print("retrieveVariable: identifier", identifier, "not found")
            return None

            # Visit a parse tree produced by FspowParser#prog.
    def visitProg(self, ctx:FspowParser.ProgContext):
        """
        One child: the stat line
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statAssignment.
    def visitStatAssignment(self, ctx:FspowParser.StatAssignmentContext):
        """
        One child: Assignment command (x = 5)
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statApplySelector.
    def visitStatApplySelector(self, ctx:FspowParser.StatApplySelectorContext):
        """
        One child: wombats.apply(Selector())
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#print.
    def visitPrint(self, ctx:FspowParser.PrintContext):
        """
        one child   :   print statement
        """

        #print(ctx.getChild(0).getText())
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#statLoop.
    def visitStatLoop(self, ctx:FspowParser.StatLoopContext):
        """
        One child: for ID in range( expression ):
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#assignment.
    def visitAssignment(self, ctx:FspowParser.AssignmentContext):
        """
        Minimum 3 children:
            0   :   variable
            1   :   '='
            2   :   expression
            *   :   Chilren 1 and 2 again
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))

        ID = ctx.getChild(0).getText()
        value = self.visit(ctx.getChild(2))
        self.variablesTable[ID] = value
        return True # for now


    # Visit a parse tree produced by FspowParser#fcApplySelector.
    def visitFcApplySelector(self, ctx:FspowParser.FcApplySelectorContext):
        """
        Children:
            0   :   ID
            1   :   '.apply('
            2   :   expression
            3   :   ')'
        """

#         todo: use retrieveVariable
        fileCollectionIdentifier = ctx.getChild(0).getText()
        if fileCollectionIdentifier in self.variablesTable:
            # apply selector
            selector = self.retrieveVariable(ctx.getChild(2).getText())
            
            # How could I get a list of Selectors?
            # selector = []
            # i = 2
            # while ctx.getChild(i) != ")":
            #     selector.append(self.visit(ctx.getChild(i)))
            #     i = i + 1
            if isinstance(selector, Selector):
                updatedFc = self.variablesTable[fileCollectionIdentifier]
                updatedFc.apply(selector)
                self.variablesTable[fileCollectionIdentifier] = updatedFc
        else:
            print("visitFcApplySelector: File collection", fileCollectionIdentifier, "not found")
#         for i in range(ctx.getChildCount()):
#             print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return True


    # Visit a parse tree produced by FspowParser#exprID.
    def visitExprID(self, ctx:FspowParser.ExprIDContext):
        """
        One child: ID
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNewSelector.
    def visitExprNewSelector(self, ctx:FspowParser.ExprNewSelectorContext):
        """
        One child: new Selector statment
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNewFileCollection.
    def visitExprNewFileCollection(self, ctx:FspowParser.ExprNewFileCollectionContext):
        """
        3 children:
            0   :   'FileCollection'
            1   :   ID
            2   :   ')'
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprNumeric.
    def visitExprNumeric(self, ctx:FspowParser.ExprNumericContext):
        """
        One child   :   assignment with out the '='
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#exprlength.
    def visitExprlength(self, ctx:FspowParser.ExprlengthContext):
        """
        One child: 'ID.length()'
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#variable.
    def visitVariable(self, ctx:FspowParser.VariableContext):
        """
        One child: ID
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))

        identifier = ctx.getChild(0).getText()
        if identifier in self.variablesTable:
            return self.variablesTable[identifier]
        else:
            print("visitVariable: variable with identifier %s not found" % (identifier))
            return None
            
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

        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))

        # Return selectors
        sType = self.visit(ctx.getChild(1))
#        print(sType)
        newSelector = Selector(sType)
#        print(newSelector.__str__())
        return newSelector


    # Visit a parse tree produced by FspowParser#selectorType.
    def visitSelectorType(self, ctx:FspowParser.SelectorTypeContext):
        """
        Children:
            0   :   'name('
            1   :   STRING
            2   :   ')'
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return ctx.getChild(1).getText()


    # Visit a parse tree produced by FspowParser#newFileCollection.
    def visitNewFileCollection(self, ctx:FspowParser.NewFileCollectionContext):
        """
        Children:
            0   :   'FileCollection('
            1   :   root specifier
            2   :   ')'
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))

        rootName = str(self.visitRootSpecifier(ctx.getChild(1)))
        fc = FileCollection(rootName)
        # print(fc.list())
        return fc
         


    # Visit a parse tree produced by FspowParser#rootSpecifier.
    def visitRootSpecifier(self, ctx:FspowParser.RootSpecifierContext):
        """
        One child   :   ID
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        
        retval = ctx.getChild(0)
        return retval


    # Visit a parse tree produced by FspowParser#numeric.
    def visitNumeric(self, ctx:FspowParser.NumericContext):
        """
        Minimum children 1:
            0   :   label (INTEGER or ID)
            +   :   operator
            +   :   label 
        """
        numeric = ctx.getChild(0).getText()
        return numeric
        
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        
        


    # Visit a parse tree produced by FspowParser#operator.
    def visitOperator(self, ctx:FspowParser.OperatorContext):
        """
        One child   :   operator ('+', '-', '*', '/')
        """
        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
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

        Type C: print wombats[x]
            0   :   'print'
            1   :   fc_name
            2   :   '['
            3   :   index_name (INTEGER or ID)
            4   :   ']'

        Type D: print len(wombats)
            0   :   'print '
            1   :   'len(' ID ')'
        """
        
        if ctx.getChildCount() == 2:
            theMessage = str(ctx.getChild(1))
            meep = self.visit(ctx.getChild(1))
            if type(meep) is int:
                # print len(ID)
                print(meep)
            else:
                if theMessage in self.variablesTable:
                    # print ID
                    ID = self.retrieveVariable(theMessage)
                    if type(ID) is str:
                        print(ID)
                    elif type(ID) is int:
                        print(ID)
                    elif type(ID) is FileCollection:
                        print(ID.list())         
                else:
                    # print STRING
                    print(theMessage)
        elif ctx.getChildCount() == 5:
            # print wombats[ID]

            # Strings taken from statment
            fc_name = str(ctx.getChild(1))
            index_name = str(ctx.getChild(3))

            # retrive FileCollection
            fc = self.retrieveVariable(fc_name)

            # Decision making between variable or integer
            if fc_name in self.variablesTable:
                if index_name in self.variablesTable:
                    # If it is a variable
                    index = self.retrieveVariable(index_name)
                    if index == None:
                        print("visitPrints: index out of bounds")
                    else:
                        result = fc.__getitem__(int(index))
                        print(result)
                else:
                    # If it is a integer
                    #print(index_name)

                    try:
                        result = fc.__getitem__(int(index_name))
                        if result == None:
                            print("visitPrints: index out of bounds")
                        else:
                            print(result)
                    except ValueError:
                        index = self.retrieveVariable(index_name)
                        if index == None:
                            print("visitPrints: index out of bounds")
                        else:
                            result = fc.__getitem__(int(index))
                            print(result)
            else:
                print("visitPrints: File collection", fc, "not found")

        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FspowParser#loop.
    def visitLoop(self, ctx:FspowParser.LoopContext):
        """
        Children:
            0   :   'for'
            1   :   ID
            2   :   ' in range('
            3   :   length or INTEGER
            4   :   '):'
            5   :   stat*
        """

        index = str(ctx.getChild(1))
        curIndex = int(self.retrieveVariable(index))
        condition = self.visit(ctx.getChild(3))

        # print(curIndex)
        # print(type(condition))

        # If index don't exist, make a new one starting from 0
        # if index in self.variablesTable:
        #     print("Creating new variable called " + index)
        #     self.variablesTable[index] = 0
        #     curIndex = self.retrieveVariable(index)

        # If index is a variable begin to loop
        if index in self.variablesTable:
            # Visit children in loop
            f = 5
            for f in range(ctx.getChildCount()):
                self.visit(ctx.getChild(f))

            # Update loop
            self.variablesTable[index] = curIndex + 1

            # Recurse until length
            length = condition
            if curIndex < length-1:
                self.visitLoop(ctx)
            else:
                # Returns variable back to normal at the end
                self.variablesTable[index] = curIndex - length + 1
        else:
            # else error thrown
            print("visitLoop: Please assign a numeric to loop")

        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
    
        return True


    # Visit a parse tree produced by FspowParser#length.
    def visitLength(self, ctx:FspowParser.LengthContext):
        """
        Children:
            0   :   'len('
            1   :   ID
            2   :   ')'
        """
        identifier = ctx.getChild(1).getText()
        
        if identifier in self.variablesTable:
            ID = self.retrieveVariable(identifier)
            return ID.length()
        else:
            print("visitLength: variable with identifier %s not found" % (identifier))
            return None

        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by FspowParser#label.
    def visitLabel(self, ctx:FspowParser.LabelContext):
        """
        One child   :   label (INTEGER or ID)
        """

        # for i in range(ctx.getChildCount()):
        #     print("%s:\t%d:\t%s" % (sys._getframe().f_code.co_name, i, ctx.getChild(i).getText()))
        return self.visitChildren(ctx)
        
del FspowParser
