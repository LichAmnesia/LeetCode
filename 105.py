# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 19:02:16
# @Last Modified time: 2016-10-07 20:24:26
# @FileName: 105.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dic = {}

        for i in range(len(inorder)):
            dic[inorder[i]] = i

        def build(s0, e0, s1, e1):
            if s0 > e0 or s1 > e1: 
                return None

            root = TreeNode(preorder[s1])

            mid = dic[preorder[s1]]
            num = mid - s0

            root.left = build(s0, mid - 1, s1 + 1, s1 + num)
            root.right = build(mid + 1, e0, s1 + num + 1, e1)

            return root

        return build(0, len(inorder) - 1, 0, len(preorder) - 1)