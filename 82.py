# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-20 00:55:16
# @Last Modified time: 2016-10-20 00:59:55
# @FileName: 82.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        new_head = ListNode(0)
        new_head.next = head
        parent = new_head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                val = cur.val
                # print val
                while cur and val == cur.val:
                    cur = cur.next
                parent.next = cur
            else:
                parent = parent.next
                cur = cur.next
        return new_head.next