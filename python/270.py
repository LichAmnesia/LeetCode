# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 17:00:28
# @Last Modified time: 2016-11-17 17:00:29
# @FileName: 270.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root: return 0
        
        def dfs(r, target):
            kid = r.left if target < r.val else  r.right
            if not kid: return r.val
            
            close = dfs(kid, target)
            return close if abs(close - target) < abs(r.val - target) else r.val
            
        return dfs(root, target)