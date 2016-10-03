# -*- coding: utf-8 -*-
# @Author: lich
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 17:47:29
# @Last Modified by:   lich
# @Last Modified time: 2016-10-02 18:03:27


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]

        def dfs(mini, res):
            for i in range(mini, len(nums)):
                res.append(nums[i])
                ans.append(res)
                dfs(i + 1, res)

        for i in range(len(nums)):
            dfs(i, [])

        return ans