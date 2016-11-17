# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 11:22:54
# @Last Modified time: 2016-11-17 11:22:55
# @FileName: 281.py

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data = [x for pair in zip(v1, v2) for x in pair]
        self.idx = 0
        if len(v1) > len(v2):
            self.data.extend(v1[len(v2):])
        else:
            self.data.extend(v2[len(v1):])
            

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            return 0
        
        res = self.data[self.idx]
        self.idx += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.data) 

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())