# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 12:57:48
# @Last Modified time: 2016-09-22 13:08:56
# @FileName: 112.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        def dfs(root, add):
            if not root:
                if add == sum:
                    return True
                else:
                    return False
            if root.left and root.right:
                return any([dfs(root.left, add + root.val), dfs(root.right, add + root.val)])
            

        return dfs(root, 0)
