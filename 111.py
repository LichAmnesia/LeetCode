# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 21:39:06
# @Last Modified time: 2016-09-22 21:44:54
# @FileName: 111.py


# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 21:26:50
# @Last Modified time: 2016-09-22 21:38:18
# @FileName: 257.py


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        def dfs(r):
            if not r.left and not r.right:
                return 1
            if r.left and r.right:
                return min(dfs(r.left), dfs(r.right)) + 1
            if r.right:
                return dfs(r.right) + 1
            if r.left:
                return dfs(r.left) + 1

        return dfs(root)
