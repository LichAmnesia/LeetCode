# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 22:48:05
# @Last Modified time: 2016-10-19 22:48:08
# @FileName: 98.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, start, end):
            if not root:
                return True
            if root.left and (root.left.val >= root.val or root.left.val <= start):
                return False
            if root.right and (root.right.val <= root.val or root.right.val >= end):
                return False
            leftEnd = end
            rightStart = start
            if root.val < end:
                leftEnd = root.val
            if root.val > start:
                rightStart = root.val
            return all([dfs(root.left, start, leftEnd), dfs(root.right, rightStart, end)])

        return dfs(root, -sys.maxint, sys.maxint)
