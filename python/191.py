# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 16:08:04
# @Last Modified time: 2016-09-18 17:37:58
# @FileName: 191.py


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            if n % 2 == 1:
                n /= 2
                res += 1
            else:
                n /= 2
        return res