# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 21:31:28
# @Last Modified time: 2016-10-01 21:33:54
# @FileName: 334.py
# 维护一个最小值和第二小值


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1 = sys.maxint
        m2 = sys.maxint
        for i in range(len(nums)):
            if nums[i] <= m1:
                m1 = nums[i]
            elif nums[i] <= m2:
                m2 = nums[i]
            else:
                return True
        return False
