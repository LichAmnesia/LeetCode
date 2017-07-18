# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 11:13:13
# @Last Modified time: 2016-10-02 11:16:51
# @FileName: 53.py


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ = nums[0]
        sum_ = 0  
        for i in range(len(nums)):  
            if sum_ < 0:
                sum_ = nums[i]
            else:
                sum_ = sum_ + nums[i]
            max_ = max(sum_, max_)
        return max_
