# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 17:22:49
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-05 17:33:29


class Solution(object):

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 1:
            return []
        dp = [1 for x in range(len(nums))]
        dp[0] = 1
        nums = sorted(nums)
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        maxIndex = dp.index(max(dp))
        ans = [nums[maxIndex]]
        for i in range(maxIndex, -1, -1):
            if nums[maxIndex] % nums[i] == 0 and dp[i] + 1 == dp[maxIndex]:
                ans.append(nums[i])
                dp[maxIndex] = dp[i]
        return ans
