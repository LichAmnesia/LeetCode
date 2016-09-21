# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 19:46:05
# @Last Modified time: 2016-09-20 19:49:16
# @FileName: 172.py


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            n /= 5
            res += n
        return res