# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-16 00:03:58
# @Last Modified time: 2016-09-16 00:04:41
# @FileName: 217.py


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False