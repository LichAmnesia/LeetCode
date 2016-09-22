# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 12:01:29
# @Last Modified time: 2016-09-22 12:16:28
# @FileName: 101.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def isSame(self, left, right):
        if left == right:
            return True
        if left and right and left.val == right.val:
            return self.isSame(left.left, right.right) and self.isSame(left.right, right.left)
        return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSame(root.left, root.right)
