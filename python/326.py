# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-15 21:56:59
# @Last Modified time: 2016-09-15 23:56:37
# @FileName: 326.py


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        tmp = math.log10(n) / math.log10(3)
        return tmp.is_integer()
