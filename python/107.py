# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 12:40:19
# @Last Modified time: 2016-09-22 12:57:42
# @FileName: 107.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        dic = {}
        # level = 0
        if not root:
            return [[]]
        # dic[level].append(root.val)

        def dfs(root, level):
            if not root:
                return
            elif level in dic:
                dic[level].append(root.val)
            else:
                dic[level] = [root.val]
            if root.left:
                dfs(root.left, level + 1)
                # dic[level + 1].append(root.left.val)
            if root.right:
                dfs(root.right, level + 1)
                # dic[level + 1].append(root.right.val)

        dfs(root, 0)

        ans_list = [dic[l] for l in sorted(dic, reverse=True)]
        return ans_list
