# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:54:00
# @Last Modified time: 2016-10-21 22:54:06
# @FileName: 92.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head.next is None or head is None or n - m < 1:
            return head
        dummpy = ListNode(0)
        dummpy.next = head
        now = dummpy
        for i in range(m - 1):
            now = now.next
        
        pre = now.next
        origin = now
        now = pre.next
        # print now.val,origin.val
        for i in range(n - m):
            tmp = now.next
            now.next = pre
            pre = now
            now = tmp
            # print i, pre.val, now.val
        # print pre.val, now.val
        origin.next.next = now
        origin.next = pre
        return dummpy.next