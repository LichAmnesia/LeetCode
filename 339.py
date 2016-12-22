# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-22 11:04:03
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-22 11:04:04
# @Email: shen.huang@colorado.edu


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        # ans = 0
        
        def dfs(nestedList, dep):
            ans = 0
            for i in range(len(nestedList)):
                if nestedList[i].isInteger():
                    ans += nestedList[i].getInteger() * dep;
                else:
                    ans += dfs(nestedList[i].getList(), dep + 1)
            return ans
        
        return dfs(nestedList, 1)
        # return ans
        