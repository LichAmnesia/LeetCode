# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 01:36:32
# @Last Modified time: 2016-10-06 01:42:19
# @FileName: 129.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []

        def dfs(r, val):
            if not r:
                return 
            if not r.left and not r.right:
                ans.append(val + str(r.val))
            dfs(r.left, val + str(r.val))
            dfs(r.right, val + str(r.val))

        dfs(root, '')
        return sum([int(x) for x in ans])
