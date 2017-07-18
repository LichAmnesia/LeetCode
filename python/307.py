# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-22 23:38:43
# @Last Modified time: 2016-10-22 23:38:50
# @FileName: 307.py


class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.bit = [0] * (len(nums) + 1)
        self.nums = [0] * (len(nums) + 1)
        self.n = len(nums)
        for idx, val in enumerate(nums):
            self.update(idx, val)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        i += 1
        diff = val - self.nums[i]
        self.nums[i] = val
        while i <= self.n:
            self.bit[i] += diff
            i += i & -i

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j + 1) - self.sum(i)

    def sum(self, i):
        res = 0
        while i:
            res += self.bit[i]
            i -= i & -i
        return res

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
