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
    # @param {TreeNode} root
    # @return {string[]}

    def binaryTreePaths(self, root):
        ans = []
        if root is None:
            return []
        path = str(root.val)

        def dfs(r, path):
            if not r.left and not r.right:
                ans.append(path)
                return
            if r.left:
                dfs(r.left, path + "->" + str(r.left.val))
            if r.right:
                dfs(r.right, path + "->" + str(r.right.val))

        dfs(root, path)
        return ans
