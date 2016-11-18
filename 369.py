# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-18 11:43:29
# @Last Modified time: 2016-11-18 11:43:30
# @FileName: 369.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        dummpy = ListNode(0)
        dummpy.next = head
        dummpy = self.reverse(dummpy)
        now = dummpy.next
        now.val += 1
        
        now = dummpy.next
        while now:
            print now.val
            if now.val >= 10:
                now.val -= 10
                if now.next:
                    now = now.next
                    now.val += 1
                else:
                    now.next = ListNode(1)
                    now = now.next
                    break
            else:
                break
        dummpy = self.reverse(dummpy)
        return dummpy.next
        
    def reverse(self, head):
        pre = head.next
        now = pre.next
        first = pre
        while now:
            tmp = now.next
            now.next = pre
            pre = now
            now = tmp
        first.next = None
        head.next = pre
        
        
        return head