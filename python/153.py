# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 23:29:19
# @Last Modified time: 2016-10-02 00:33:07
# @FileName: 153.py


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]: #min 位于左侧
                high = mid
            else: #min位于左侧上升沿与右侧上升沿之间
                low = mid + 1
        return nums[low]