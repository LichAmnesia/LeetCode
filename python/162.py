# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 23:08:03
# @Last Modified time: 2016-10-05 23:58:29
# @FileName: 162.py


class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        l = 0
        r = len(nums) - 1
        mid = 0
        while l <= r:
            mid = (l + r) / 2
            if (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]) and (mid == 0 or nums[mid] > nums[mid - 1]):
                return mid
            if mid > 0 and nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                l = mid + 1
        return mid
