# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-17 09:12:24
# @Last Modified time: 2016-09-17 09:16:07
# @FileName: 83.py


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
        pre = None
        node = head
        while node:
            if pre and node.val == pre.val:
                node, pre.next = node.next, node.next
            else:
                pre, node = node, node.next
        return head 