# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 17:19:43
# @Last Modified time: 2016-09-24 17:41:37
# @FileName: 268.py


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while nums[i] != i and nums[i] < len(nums):
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return n