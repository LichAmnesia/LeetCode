# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 01:42:15
# @Last Modified time: 2016-10-07 02:02:26
# @FileName: 113.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
                
        if root is None:
            return []

        ans = []
        def dfs(root, add, path):
            if not root:
                return
            if root.left is None and root.right is None and add + root.val == sum:
                path.append(root.val)
                ans.append([x for x in path])
                path.pop()
                return 
            path.append(root.val)
            dfs(root.left, add + root.val, path)
            dfs(root.right, add + root.val, path)
            path.pop()

        dfs(root, 0, [])
        return ans