# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 01:52:11
# @Last Modified time: 2016-09-20 01:56:19
# @FileName: 235.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p
        if root.val >= p.val and root.val <= q.val:
            return root
        return self.lowestCommonAncestor(root.left, p, q) if root.val > q.val else self.lowestCommonAncestor(root.right, p, q)
