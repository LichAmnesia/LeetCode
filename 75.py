# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-04 08:49:08
# @Last Modified time: 2016-09-04 08:59:58
# @FileName: 75.py


# k0 k1 k2 for 0 1 2 num
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k0 = 0
        k1 = 0
        for k2 in range(len(nums)):
            if nums[k2] == 0:
                if nums[k0] == 1:
                    if nums[k0 + k1] == 2:
                        nums[k2] = 2
                    nums[k0 + k1] = 1
                elif nums[k0] == 2:
                    nums[k2] = 2
                nums[k0] = 0
                k0 += 1
            elif nums[k2] == 1:
                if nums[k0 + k1] == 2:
                    nums[k2] = 2
                nums[k0 + k1] = 1
                k1 += 1
