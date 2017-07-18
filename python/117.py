# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 02:16:23
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 02:16:33
# https://siddontang.gitbooks.io/leetcode-solution/content/tree/populating_next_right_pointers_in_each_node.html

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
        if not root:
            return

        p = root
        first = None
        last = None
        while p:
            # 设置下层第一个元素
            if not first:
                if p.left or p.right:
                    first = p.left if p.left else p.right

            if p.left:
                # if has last then last is p.left
                if last:
                    last.next = p.left
                # update last
                last = p.left

            if p.right:
                if last:
                    last.next = p.right
                last = p.right

            if p.next:
                p = p.next
            else:
                p = first
                first = None
                last = None
