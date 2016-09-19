# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 23:03:45
# @Last Modified time: 2016-09-18 23:11:57
# @FileName: 234.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow, pre = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            pre, slow.next, slow = slow, pre, slow.next
        if fast:
            slow = slow.next
        while pre and pre.val == slow.val:
            pre, slow = pre.next, slow.next
        return not pre