# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 14:38:58
# @Last Modified time: 2016-09-20 14:50:43
# @FileName: 160.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a, b = headA, headB
        t1, t2 = headA, headB
        while t1 and t2:
            t1 = t1.next
            t2 = t2.next
        while t1:
            t1 = t1.next
            a = a.next
        while t2:
            t2 = t2.next
            b = b.next
        while a != b:
            a = a.next
            b = b.next
        return a
