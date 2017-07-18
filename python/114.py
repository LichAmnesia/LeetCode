# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 17:47:40
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-05 17:57:55


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    node = None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return None
            l = root.left
            r = root.right
            if self.node is None:
                self.node = root
            else:
                self.node.left, self.node.right = None, root
                self.node = root
            dfs(l)
            dfs(r)

        dfs(root)