# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-16 00:10:26
# @Last Modified time: 2016-09-16 01:42:21
# @FileName: 169.py


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]] += 1
            else:
                m[nums[i]] = 1
        label = sorted(m, key=m.__getitem__, reverse=True)
        return label[0]
