# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-29 00:09:04
# @Last Modified time: 2016-09-29 00:14:07
# @FileName: 144.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans

        def pre(r):
            if r:
                ans.append(r.val)
            if r.left:
                pre(r.left)
            if r.right:
                pre(r.right)
        
        pre(root)
        return ans
