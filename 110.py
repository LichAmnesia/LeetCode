# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 18:05:14
# @Last Modified time: 2016-09-22 18:24:28
# @FileName: 110.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def depth(root):
            if not root:
                return 0, True
            depL, isL = depth(root.left)
            depR, isR = depth(root.right)
            if abs(depL - depR) <= 1 and isL and isR:
                return max(depL, depR) + 1, True
            else:
                return max(depL, depR) + 1, False

        dep, isB = depth(root)
        return isB
