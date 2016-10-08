# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 19:04:33
# @Last Modified time: 2016-10-07 19:06:56
# @FileName: 106.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        dic = {}

        for i in range(len(inorder)):
            dic[inorder[i]] = i

        def build(s0, e0, s1, e1):
            if s0 > e0 or s1 > e1: 
                return None

            root = TreeNode(postorder[e1])

            mid = dic[postorder[e1]]
            num = mid - s0

            root.left = build(s0, mid - 1, s1, s1 + num - 1)
            root.right = build(mid + 1, e0, s1 + num, e1 - 1)

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)