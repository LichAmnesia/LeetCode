# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 15:04:32
# @Last Modified time: 2016-11-29 12:56:33
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


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans, ranges = [], []
        for i in range(len(nums)):
            if nums[i] - 1 not in ranges:
                ans.append(ranges[:])
                print(ans)
                ranges = [nums[i]]
            else:
                if len(ranges) < 2:
                    ranges.append(nums[i])
                else:
                    ranges[1] = nums[i]
                print(ranges)
        ans.append(ranges[:])
        print(ans)
        res = []
        for x in ans:
            if x:
                if type(x) == int:
                    res.append(str(x))
                else:
                    res.append('->'.join(map(str,x)))
        return res