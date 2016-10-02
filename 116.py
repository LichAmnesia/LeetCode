# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 11:27:44
# @Last Modified time: 2016-10-02 11:41:16
# @FileName: 116.py


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        if root is None:
            return
        pre, now = [], [root]
        while len(now):
            for i in range(len(now)):
                if i == len(now) - 1:
                    now[i].next = None
                else:
                    now[i].next = now[i + 1]
                if now[i].left:
                    pre.append(now[i].left)
                if now[i].right:
                    pre.append(now[i].right)
            now = pre
            pre = []
