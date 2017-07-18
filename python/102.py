# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 18:22:07
# @Last Modified time: 2016-09-22 18:52:30
# @FileName: 102.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = {}
        if not root:
            return []

        def dfs(r, dep):
            if not r:
                return
            if dep in dic:
                dic[dep].append(r.val)
            else:
                dic[dep] = [r.val]
            if r.left:
                dfs(r.left, dep + 1)
            if r.right:
                dfs(r.right, dep + 1)

        dfs(root, 0)

        ans = [dic[i] for i in dic]
        return ans

