# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-15 23:51:46
# @Last Modified time: 2016-10-15 23:55:54
# @FileName: 222.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root):
            if root is None: return 0
            hl, hr = 0, 0
            le, ri = root, root
            while le: 
                le = le.left
                hl += 1
            while ri: 
                ri = ri.right
                hr += 1
            if hr == hl:
                return 2 ** hl  - 1
            return 1 + dfs(root.left) + dfs(root.right)

        return dfs(root)