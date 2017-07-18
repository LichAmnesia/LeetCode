# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 17:31:17
# @Last Modified time: 2016-11-09 21:48:13
# @FileName: 274.py


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        nums = sorted(citations, reverse=True)
        for i in range(len(nums)):
            if i >= nums[i]:
                return i
        return len(nums)