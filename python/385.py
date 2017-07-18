# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-20 17:43:30
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-20 17:43:35


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack = []
        sign = 1
        num = None
        for i in range(len(s)):
            if s[i] == '-':
                sign = -1
            elif s[i] >= '0' and s[i] <= '9':
                num = (num or 0) * 10 + ord(s[i]) - ord('0')
            elif s[i] == '[':
                stack.append(NestedInteger())
            else:
                if num is not None:
                    stack[-1].add(NestedInteger(sign * num))
                    num, sign = None, 1
                if s[i] == ']':
                    top = stack.pop()
                    print top
                    if stack:
                        stack[-1].add(top)
                    else:
                        return top
        return NestedInteger(sign * (num or 0))
