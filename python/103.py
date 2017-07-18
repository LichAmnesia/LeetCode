# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 22:24:28
# @Last Modified time: 2016-10-19 22:24:32
# @FileName: 103.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        level = [root]
        direction = 1
        while level:
            ans.append([node.val for node in level][::direction])
            direction *= -1
            level = [kid for node in level for kid in [
                node.left, node.right] if kid]
        return ans
