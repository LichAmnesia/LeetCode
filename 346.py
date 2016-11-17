# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 11:00:33
# @Last Modified time: 2016-11-17 11:00:34
# @FileName: 346.py


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.q = collections.deque()
        self.sum_ = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.q) == self.size:
            a = self.q.popleft()
            self.sum_ -= a
        self.q.append(val)
        self.sum_ += val
        return float(self.sum_) / len(self.q)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)