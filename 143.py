# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-15 14:39:16
# @Last Modified time: 2016-09-15 16:48:10
# @FileName: 143.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        pre = None
        while slow:
            pre, slow.next, slow = slow, pre, slow.next

        # merge
        slow = pre
        while slow.next:
            head.next, head = slow, head.next
            slow.next, slow = head, slow.next
