# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 15:28:39
# @Last Modified time: 2016-09-24 15:33:15
# @FileName: 303.py


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if len(nums) < 1:
            self.sum = [0]
            return
        self.sum = [0 for x in nums]
        self.sum[0] = nums[0]
        for i in range(1, len(nums)):
            self.sum[i] = nums[i] + self.sum[i - 1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum[j] - self.sum[i - 1] if i > 0 else self.sum[j]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)