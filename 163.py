# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 11:10:14
# @Last Modified time: 2016-11-17 11:10:15
# @FileName: 163.py



class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.insert(0, lower - 1)
        nums.append(upper + 1)
        i, j = 0, 1
        ans = []
        while j < len(nums):
            if nums[j] - nums[i] == 2:
                ans.append(str(nums[i] + 1))
            elif nums[j] - nums[i] > 2:
                ans.append(str(nums[i] + 1) + '->' + str(nums[j] - 1))
            i += 1
            j += 1
        return ans