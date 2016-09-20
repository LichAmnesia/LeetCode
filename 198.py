# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 02:07:17
# @Last Modified time: 2016-09-20 02:15:18
# @FileName: 198.py


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        dp = [[] for x in range(len(nums))]
        dp[0] = [0, nums[0]]
        for i in range(1, len(nums)):
            dp[i] = [max(dp[i - 1][0], dp[i - 1][1]), dp[i - 1][0] + nums[i]]
        return max(dp[len(nums) - 1][0], dp[len(nums) - 1][1])
