# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 23:12:39
# @Last Modified time: 2016-09-18 23:19:24
# @FileName: 203.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre, node = None, head
        while node:
            if node.val == val:
                if node.next:
                    node.val, node.next = node.next.val, node.next.next
                else:
                    if pre and pre.next:
                        pre.next = None
                        node = None
                    else:
                        return pre
            else:
                pre, node = node, node.next
        return head