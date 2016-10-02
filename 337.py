# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 18:52:54
# @Last Modified time: 2016-10-01 19:54:47
# @FileName: 337.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        memo = {}

        def dfs(r, flag):
            if r is None:
                return 0
            if flag:
                if r not in memo:
                    memo[r] = max(r.val + dfs(r.left, not flag) + dfs(r.right,
                                                                      not flag), dfs(r.left, flag) + dfs(r.right, flag))
                return memo[r]
            else:
                return dfs(r.left, not flag) + dfs(r.right, not flag)

        return max(dfs(root, True), dfs(root, False))
