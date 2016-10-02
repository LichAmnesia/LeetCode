# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 22:44:18
# @Last Modified time: 2016-10-01 23:07:31
# @FileName: 108.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) < 1:
            return None
        def build(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
                
            mid = (l + r) / 2
            node = TreeNode(nums[mid])
            
            
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            
            return node

        root = build(0, len(nums) - 1)
        return root
