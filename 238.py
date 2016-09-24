# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-23 21:01:14
# @Last Modified time: 2016-09-23 21:21:10
# @FileName: 238.py


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        output = []
        for i in range(0, len(nums)):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output