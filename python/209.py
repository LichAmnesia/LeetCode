# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 15:13:51
# @Last Modified time: 2016-10-07 15:13:52
# @FileName: 209.py


class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        start, end, sum = 0, 0, 0
        bestAns = size + 1
        while end < size:
            while end < size and sum < s:
                sum += nums[end]
                end += 1
            while start < end and sum >= s:
                bestAns = min(bestAns, end - start)
                sum -= nums[start]
                start += 1
        return [0, bestAns][bestAns <= size]