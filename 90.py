# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-11 20:27:45
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-11 20:27:59


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        for num in nums:
            
