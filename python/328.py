# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-29 00:20:17
# @Last Modified time: 2016-09-29 00:52:34
# @FileName: 328.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None or head.next.next is None:
            return head
        odd, even = head, head.next
        while even.next:
            tmp = odd.next
            odd.next, even.next  = even.next, even.next.next
            odd = odd.next
            odd.next = tmp
            if even.next:
                even = even.next
        return head