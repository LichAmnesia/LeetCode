# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-26 19:52:48
# @Last Modified time: 2016-10-26 19:52:50
# @FileName: 146.py


class LinkedNode:

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # hash
        # key: key
        # value: prev ListNode in the linkedlist
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    def updateLink(self, pre):
        node = pre.next
        # if already tail, no need to update
        if node == self.tail:
            return
        else:
            pre.next = node.next
            if node.next:
                self.hash[node.next.key] = pre

    def pushTail(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node
        node.next = None

    def popFront(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.hash:
            return -1
        else:
            pre = self.hash[key]
            node = pre.next
            if node != self.tail:
                self.updateLink(pre)
                self.pushTail(node)
            return self.hash[key].next.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        # write your code here
        if key in self.hash:
            #key in hash
            # 1. update node's prev and next
            # 2. put node to tail
            prev = self.hash[key]
            node = prev.next
            if node != self.tail:
                self.updateLink(prev)
                self.pushTail(node)
            self.hash[key].next.value = value
        else:
            node = LinkedNode(key, value)
            # 1. put node to tail
            # 2. if size > cap, pop lru node
            self.pushTail(node)
            if len(self.hash) > self.capacity:
                self.popFront()
