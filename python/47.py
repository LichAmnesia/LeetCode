# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:54:22
# @Last Modified time: 2016-10-21 22:54:29
# @FileName: 47.py


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        
        def dfs(nums):
            vis = set()
            ans = []
            
            for idx, val in enumerate(nums):
                if val in vis:
                    continue
                vis.add(val)
                ans += [[val] + path for path in dfs(nums[:idx]+nums[idx+1:]) or [[]] ]
            return ans
        
        return dfs(nums)
        