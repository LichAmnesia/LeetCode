# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-16 01:46:35
# @Last Modified time: 2016-09-16 01:47:45
# @FileName: 258.py


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        while num:
            t = num % 10
            num /= 10
            sum += t
            if sum >= 10:
                sum -= 9
        return sum
