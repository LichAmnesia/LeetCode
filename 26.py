# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 20:43:49
# @Last Modified time: 2016-09-22 21:26:42
# @FileName: 26.py


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for i in nums:
            s.add(i)
        return len(s)