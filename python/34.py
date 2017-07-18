# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 01:06:30
# @Last Modified time: 2016-10-04 01:24:29
# @FileName: 34.py


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] <= target:
                r = mid - 1
            else:
                l = mid + 1
        if l < len(nums) and nums[l] == target:
            min_ = l
        else:
            min_ = -1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] < target:
                r = mid - 1
            else:
                l = mid + 1
        if r >= 0 and nums[r] == target:
            max_ = r
        else:
            max_ = -1
        if min_ == -1 or max_ == -1:
            return [-1, -1]
        ans = [nums[x] for x in range(min_, max_ + 1)]
        return ans
        
