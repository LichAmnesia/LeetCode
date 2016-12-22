# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-22 11:26:22
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-22 11:26:24
# @Email: shen.huang@colorado.edu



# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
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
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        ans = collections.defaultdict()
        self.max_dep = 0 
        def dfs(nestedList, dep):
            self.max_dep = max(self.max_dep, dep)
            for i in range(len(nestedList)):
                if nestedList[i].isInteger():
                    if dep not in ans:
                        ans[dep] = nestedList[i].getInteger()
                    else:
                        ans[dep] += nestedList[i].getInteger()
                    # a);
                else:
                    dfs(nestedList[i].getList(), dep + 1)
            
        dfs(nestedList, 1)
        max_dep = self.max_dep + 1
        res = 0
        for k in ans:
            res += ans[k] * (max_dep - k)
        return res
        