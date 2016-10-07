# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 15:04:32
# @Last Modified time: 2016-10-07 15:13:44
# @FileName: 228.py


class Solution(object):

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans, ranges = [], []
        for i in range(len(nums)):
            if nums[i] - 1 not in ranges:
                ranges = [nums[i]]
                ans += ranges
            ranges[1:] = nums[i]
        return ['->'.join(map(str, r)) for r in ans]
