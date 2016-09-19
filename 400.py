# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 21:41:06
# @Last Modified time: 2016-09-18 22:24:12
# @FileName: 400.py


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = [0]
        for i in range(1, 10):
            tmp = 10 ** i - 10 ** (i - 1)
            tmp *= i
            num.append(tmp)
        if n < 10:
            return n
        for i in range(len(num)):
            if n < num[i]:
                now = i - 1
                res = (n + i - 1) / i
                return int(str(10 ** now + res - 1)[(n % i - 1 + i) % i])
            else:
                n -= num[i]
