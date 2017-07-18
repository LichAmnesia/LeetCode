# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-23 20:39:28
# @Last Modified time: 2016-09-23 20:42:31
# @FileName: 397.py


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 1:
            if n == 3:
                n -= 1
            elif n % 2 == 0:
                n /= 2
            elif (n + 1) % 4 == 0:
                n += 1
            else:
                n -= 1
            res += 1
        return res