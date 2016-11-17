# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 10:51:06
# @Last Modified time: 2016-11-17 10:51:07
# @FileName: 298.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        def dfs(preVal, r, preLen):
            if not r:
                return preLen
            
            nowLen = preLen + 1 if preVal + 1 == r.val else 1
            return max(nowLen, max(dfs(r.val, r.left, nowLen), dfs(r.val, r.right, nowLen)))
        
        return dfs(root.val - 1, root, 0)