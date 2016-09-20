# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 01:02:13
# @Last Modified time: 2016-09-20 01:04:34
# @FileName: 27.py


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        pre = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[pre], pre = nums[i], pre + 1
        return pre