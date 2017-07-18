# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-23 19:12:03
# @Last Modified time: 2016-10-23 19:13:58
# @FileName: 23.py

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) < 1:
            return None
            
        return self.mergeSolve(lists, 0, len(lists) - 1)
    
    def mergeSolve(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = (start + end) / 2
        leList = self.mergeSolve(lists, start, mid)
        riList = self.mergeSolve(lists, mid + 1, end)
        
        return self.mergeTwoLists(leList, riList)
        
    def mergeTwoLists(self, le, ri):
        dummpy = ListNode(0)
        now_node = dummpy
        
        while le and ri:
            if le.val < ri.val:
                now_node.next = le
                le = le.next
            else:
                now_node.next = ri
                ri = ri.next
            now_node = now_node.next
        if le:
            now_node.next = le
        if ri:
            now_node.next = ri
        return dummpy.next