# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 22:20:26
# @Last Modified time: 2016-09-24 22:26:57
# @FileName: 94.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ans = []

        def zhongxu(r):
            if r.left:
                zhongxu(r.left)
            if r:
                ans.append(r.val)
            if r.right:
                zhongxu(r.right)

        zhongxu(root)
