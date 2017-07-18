# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-29 09:52:54
# @Last Modified time: 2016-09-29 10:01:41
# @FileName: 155.py


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur = self.getMin()
        if cur is None or cur > x:
            cur = x
        self.st.append([cur, x])

    def pop(self):
        """
        :rtype: void
        """
        self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.st) < 1:
            return None
        return self.st[-1][1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.st) < 1:
            return None
        return self.st[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()