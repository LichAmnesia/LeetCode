# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 02:12:34
# @Last Modified time: 2016-10-07 02:21:47
# @FileName: 55.py


class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False for x in nums]
        dp[0] = True
        step = nums[0]
        for i in range(0, len(nums) - 1):
            # print step, nums[i]
            if step <= 0 and nums[i] == 0:
                return False
            step = max(nums[i] - 1, step - 1)

        return True