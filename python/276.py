# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 16:55:52
# @Last Modified time: 2016-11-17 16:55:53
# @FileName: 276.py

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        a, b, c = k, k *k, 0
        if n == 0:
            return 0
        elif n == 1:
            return a
        elif n == 2:
            return b
        for i in range(2, n):
            c = (k - 1) * (a + b)
            a = b
            b = c
        return c