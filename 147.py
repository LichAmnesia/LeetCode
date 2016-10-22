# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:55:02
# @Last Modified time: 2016-10-21 22:55:03
# @FileName: 147.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        dummpy = ListNode(0)
        dummpy.next = head
        
        cur, pre = head, dummpy
        while cur.next:
            if cur.next.val < cur.val:
                pre = dummpy
                while pre.next and pre.next.val <= cur.next.val:
                    pre = pre.next
            # print pre.next.val
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                cur = cur.next
            
        return dummpy.next