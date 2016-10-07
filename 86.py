# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 18:27:58
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-06 22:49:09


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        d1 = ListNode(0)
        d2 = ListNode(0)
        p1 = d1
        p2 = d2
        while head:
            if head.val < x:
                p1.next = head
                p1.val = head.val
            else:
                p2.next = head
                p2.val = head.val
            head = head.next
        p2.next = None
        p1.next = d2.next
        return d1.next