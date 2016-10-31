# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 12:49:28
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 12:49:31


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 1 or head is None:
            return None
        dummpy = ListNode(0)
        dummpy.next = head
        cur = dummpy

        while cur is not None and cur.next is not None:
            ans_list = self.reverse(cur.next, k)
            if ans_list[2] != 0:
                ans_list = self.reverse(ans_list[0], k)
            cur.next = ans_list[0]
            cur = ans_list[1]
        return dummpy.next

    def reverse(self, head, n):
        if n < 1 or head is None:
            return None
        cur = head.next
        pre = head
        tail = head
        n -= 1

        while n > 0 and cur is not None:
            # print type(cur)
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            n -= 1

        tail.next = cur
        return [pre, tail, n]
