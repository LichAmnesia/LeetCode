# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 17:45:11
# @Last Modified time: 2016-10-04 17:50:28
# @FileName: 404.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        node = root

        def dfs(node):
            if not node:
                return
            if node.left and node.left.left is None and node.left.right is None:
                self.sum += node.left.val

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.sum
