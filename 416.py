# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 23:22:41
# @Last Modified time: 2016-10-20 00:53:06
# @FileName: 416.py


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_num = sum(nums)
        if sum_num & 1: return False
        n = sum_num / 2
        dp = [False for x in range(n + 1)]
        dp[0] = True
        for i in range(0, len(nums)):
            for j in xrange(n, nums[i] - 1, -1):
                # print j - nums[i]
                if dp[j - nums[i]]:
                    dp[j] = True
        return dp[n]