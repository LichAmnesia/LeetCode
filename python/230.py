# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 00:47:36
# @Last Modified time: 2016-10-01 13:06:36
# @FileName: 230.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.get(root, k)

    def calc(self, r):
        if r is None:
            return 0
        l = self.calc(r.left)
        r = self.calc(r.right)
        return l + r + 1

    def get(self, root, k):
        num = self.calc(root.left)
        if 1 + num==k:
            return root.val
        elif 1+num>k:
            return self.get(root.left, k)
        else:
            return self.get(root.right, k-1-num)