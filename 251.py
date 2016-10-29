# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-28 17:31:58
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-28 17:32:00


class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.nums = [x for x in vec2d if x]

    def next(self):
        """
        :rtype: int
        """
        if isinstance(self.nums[0], list):
            self.nums = self.nums[0] + self.nums[1:]

        return self.nums.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.nums) > 0


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
