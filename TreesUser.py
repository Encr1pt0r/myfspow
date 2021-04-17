#
# Copyright (c) 2012-2017 The ANTLR Project. All rights reserved.
# Use of this file is governed by the BSD 3-clause license that
# can be found in the LICENSE.txt file in the project root.
#


# A set of utility routines useful for all kinds of ANTLR trees.#
from io import StringIO
from antlr4.Token import Token
from antlr4.Utils import escapeWhitespace
from antlr4.tree.Tree import RuleNode, ErrorNode, TerminalNode, Tree, ParseTree
from antlr4.tree.Trees import *

# need forward declaration
Parser  = None

class TreesUser(Trees):

    # Print out a whole tree in prettier form
    # Based on Trees.toStringTree()
    # indent is the number of indents to use in the display
    @classmethod
    def PrettyPrint(cls, t:Tree, ruleNames:list=None, recog:Parser=None, indent:int=0):
        # indentation is the indent to actually display
        indentation = ''
        for n in range(indent):
            indentation += '   '
        if recog is not None:
            ruleNames = recog.ruleNames
        s = escapeWhitespace(cls.getNodeText(t, ruleNames), False)
        retval = indentation + s + "\n"
        if t.getChildCount()>0:
            # we have children to deal with
            for i in range(0, t.getChildCount()):
                retval += cls.PrettyPrint(t.getChild(i), ruleNames, indent=indent+1)
        return retval





    # The following to be dropped, once I know I don't want to override them and
    # don't want to look at them any more
    @classmethod
    def getNodeText(cls, t:Tree, ruleNames:list=None, recog:Parser=None):
        if recog is not None:
            ruleNames = recog.ruleNames
        if ruleNames is not None:
            if isinstance(t, RuleNode):
                if t.getAltNumber()!=0: # should use ATN.INVALID_ALT_NUMBER but won't compile
                    return ruleNames[t.getRuleIndex()]+":"+str(t.getAltNumber())
                return ruleNames[t.getRuleIndex()]
            elif isinstance( t, ErrorNode):
                return str(t)
            elif isinstance(t, TerminalNode):
                if t.symbol is not None:
                    return t.symbol.text
        # no recog for rule names
        payload = t.getPayload()
        if isinstance(payload, Token ):
            return payload.text
        return str(t.getPayload())


    # Return ordered list of all children of this node
    @classmethod
    def getChildren(cls, t:Tree):
        return [ t.getChild(i) for i in range(0, t.getChildCount()) ]

    # Return a list of all ancestors of this node.  The first node of
    #  list is the root and the last is the parent of this node.
    #
    @classmethod
    def getAncestors(cls, t:Tree):
        ancestors = []
        t = t.getParent()
        while t is not None:
            ancestors.insert(0, t) # insert at start
            t = t.getParent()
        return ancestors

    @classmethod
    def findAllTokenNodes(cls, t:ParseTree, ttype:int):
        return cls.findAllNodes(t, ttype, True)

    @classmethod
    def findAllRuleNodes(cls, t:ParseTree, ruleIndex:int):
        return cls.findAllNodes(t, ruleIndex, False)

    @classmethod
    def findAllNodes(cls, t:ParseTree, index:int, findTokens:bool):
        nodes = []
        cls._findAllNodes(t, index, findTokens, nodes)
        return nodes

    @classmethod
    def _findAllNodes(cls, t:ParseTree, index:int, findTokens:bool, nodes:list):
        from antlr4.ParserRuleContext import ParserRuleContext
        # check this node (the root) first
        if findTokens and isinstance(t, TerminalNode):
            if t.symbol.type==index:
                nodes.append(t)
        elif not findTokens and isinstance(t, ParserRuleContext):
            if t.ruleIndex == index:
                nodes.append(t)
        # check children
        for i in range(0, t.getChildCount()):
            cls._findAllNodes(t.getChild(i), index, findTokens, nodes)

    @classmethod
    def descendants(cls, t:ParseTree):
        nodes = [t]
        for i in range(0, t.getChildCount()):
            nodes.extend(cls.descendants(t.getChild(i)))
        return nodes
