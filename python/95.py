# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-11 17:54:37
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-11 18:02:52


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        memo = {}
        def dfs(l, r):
            ans = []
            if l > r: ans.append(None)
            for k in range(l, r + 1):
                left = dfs(l, k - 1)
                right = dfs(k + 1, r)
                for nodel in left:
                    for noder in right:
                        root = TreeNode(k)
                        root.left = nodel
                        root.right = noder
                        ans.append(root)
            return ans

        if n == 0:
            return []
        return dfs(1, n)