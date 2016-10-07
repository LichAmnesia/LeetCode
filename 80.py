# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 15:04:13
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-06 15:09:42


class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = 1
        res = 0
        pos = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cur += 1
                if cur > 2:
                    res += 1
                    continue
                pos += 1
            else:
                cur = 1
                pos += 1
            nums[pos] = nums[i]
        return len(nums) - res