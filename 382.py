# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-23 16:56:07
# @Last Modified time: 2016-09-23 17:02:49
# @FileName: 382.py


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.list = []
        while head:
            self.list.append(head.val)
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return self.list[random.randint(0, len(self.list) - 1)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()