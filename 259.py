# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-18 10:32:54
# @Last Modified time: 2016-11-18 10:32:56
# @FileName: 259.py


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        ans = 0
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] >= target:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < target:
                    ans += r - l
                    l += 1
        return ans