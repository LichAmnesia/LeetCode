# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-06 22:18:41
# @Last Modified time: 2016-09-07 08:20:16
# @FileName: 61.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head
        n, last = self.computerLen(head)
        k = k % n
        k = n - k
        if k == n:
            return head
        tmp = head
        for i in range(k):
            tmp = tmp.next
            last.next = ListNode(head.val)
            last = last.next
            head = head.next

        return tmp

    def computerLen(self, head):
        sum = 0
        ret = head
        last = 0
        while ret:
            sum += 1
            if ret.next is None:
                last = ret
                break
            ret = ret.next
        return sum, last
