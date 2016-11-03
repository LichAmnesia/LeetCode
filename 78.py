# -*- coding: utf-8 -*-
# @Author: lich
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 17:47:29
# @Last Modified by:   lich
# @Last Modified time: 2016-11-02 21:46:47


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(min_idx, path):
            for i in range(min_idx, len(nums)):
                path.append(nums[i])
                ans.append([x for x in path])
                dfs(i + 1, path)
                path.pop()
        
        ans = [[]]
        # for i in range(len(nums)):
        dfs(0, [])
        return ans
        
        
        