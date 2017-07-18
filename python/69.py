# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 20:45:45
# @Last Modified time: 2016-10-01 20:57:55
# @FileName: 69.py


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x / 2 + 1
        while l <= r:
            mid = (l + r) / 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
