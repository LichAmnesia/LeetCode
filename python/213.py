# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 17:34:32
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-05 17:47:34


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            return max(max(nums[0], nums[1]), nums[2])

        dp1 = [0 for x in range(len(nums))]
        dp2 = [0 for x in range(len(nums))]
        
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i -1], dp1[i - 2] + nums[i])

        dp2[1] = nums[1]
        dp2[2] = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        return max(dp1[len(nums) - 2], dp2[len(nums) - 1])
