# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-28 20:33:49
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-28 21:47:53
# @Email: shen.huang@colorado.edu


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums) - 1, 2):
            tmp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = tmp
        