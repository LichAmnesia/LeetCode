# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 15:20:00
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-06 15:24:46
# O(n) 
# exist a dp solution

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ans, i, j = 1, 1, 0
        while i < len(nums):
            if nums[j] < nums[i]:
                ans += 1
                while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
                    i += 1
            elif nums[j] > nums[i]:
                ans += 1
                while i < len(nums) - 1 and nums[i] >= nums[i + 1]:
                    i += 1
            i, j = i + 1, i
        return ans

