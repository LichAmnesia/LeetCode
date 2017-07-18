# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-11 21:00:26
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-11 21:09:38


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        

        def build(start, end):
            if start == end:
                return None

            fast, slow = start, start

            while fast != end and fast.next != end:
                slow, fast = slow.next, fast.next.next

            node = TreeNode(slow.val)
            node.left = build(start, slow)
            node.right = build(slow.next, end)

            return node

        return build(head, None)