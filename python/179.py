# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-17 11:31:50
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-17 11:31:54

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(x) for x in nums]
        nums = sorted(nums, lambda x, y: [1, -1][x + y > y + x])
        while len(nums) > 1 and nums[0] == '0':
            del nums[0]
        ans = ''.join(nums)
        
        return ans