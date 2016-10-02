# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 11:41:22
# @Last Modified time: 2016-10-02 11:45:20
# @FileName: 199.py

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Solution:
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    def rightSideView(self, root):
        if root is None:
            return []
        pre, now = [], [root]
        ans = []
        while len(now):
            for i in range(len(now)):
                if i == len(now) - 1:
                    ans.append(now[i].val)
                if now[i].left:
                    pre.append(now[i].left)
                if now[i].right:
                    pre.append(now[i].right)
            now = pre
            pre = []

        return ans