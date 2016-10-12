# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-11 21:24:06
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-11 21:26:44
# 2x = n + k2m + d
# x = n + k1m + d
# n + d = km
# n = (k - 1)m + m - d

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        low, fast = head, head

        while True:
            if fast == None or fast.next == None: return None
            low, fast = low.next, fast.next.next
            if fast == low: break

        while head != fast:
            head, fast = head.next, fast.next
        
        return head