# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 20:03:27
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-19 20:03:29


class Solution(object):

    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1, n2, n3 = -sys.maxint, -sys.maxint, -sys.maxint
        for i in nums:
            if i > n1:
                n1, n2, n3 = i, n1, n2
            elif i == n1:
                continue
            elif i > n2:
                n2, n3 = i, n2
            elif i == n2:
                continue
            elif i > n3:
                n3 = i
            elif i == n3:
                continue
        if n3 > -sys.maxint:
            return n3
        else:
            return n1
