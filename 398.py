# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 01:55:14
# @Last Modified time: 2016-10-06 02:07:51
# @FileName: 398.py


class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        count = 0
        res = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if random.randomint(1, count) == 1:
                    res = i
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)