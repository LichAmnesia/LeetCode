# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-05 22:49:55
# @Last Modified time: 2016-09-05 23:48:40
# @FileName: 152.py


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = minNum = Max = nums[0]
        for i in range(1, len(nums)):
            minNum, maxNum = min(nums[i], min(nums[i] * maxNum, nums[i] * minNum)), max(nums[i], max(nums[i] * maxNum, nums[i] * minNum))
            Max = max(Max, maxNum)
        return Max
