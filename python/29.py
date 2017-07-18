# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-18 23:24:07
# @Last Modified time: 2016-10-18 23:24:08
# @FileName: 29.py

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend < 0) ^ (divisor < 0):
            sign = -1
        else:
            sign = 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp = divisor
            i = 1
            while dividend >= tmp:
                tmp = tmp << 1
                i = i << 1
            dividend -= tmp >> 1
            res += i >> 1
        res = res if sign == 1 else - res

        if res >= 2147483647:
            return 2147483647
        return res