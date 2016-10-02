# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 20:58:00
# @Last Modified time: 2016-10-01 21:09:34
# @FileName: 377.py


class Solution(object):

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        memo = {}
        def dfs(target):
            if target == 0:
                return 1
            ans = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    if target - nums[i] not in memo:
                        memo[target - nums[i]] = dfs(target - nums[i])
                    ans += memo[target - nums[i]]
            return ans

        return dfs(target)
