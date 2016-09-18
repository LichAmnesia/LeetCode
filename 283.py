# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 15:30:02
# @Last Modified time: 2016-09-18 15:35:43
# @FileName: 283.py


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_of_zeros = 0
        for i in range(len(nums)):
            nums[i - num_of_zeros] = nums[i]
            if nums[i] is 0:
                num_of_zeros += 1
        for i in range(num_of_zeros):
            nums[len(nums) - num_of_zeros + i] = 0
