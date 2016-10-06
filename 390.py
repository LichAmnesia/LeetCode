# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 02:07:57
# @Last Modified time: 2016-10-06 02:13:08
# @FileName: 390.py


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        begin, p = 1, 1 
        cnt = 0
        while n > 1:
            n /= 2
            cnt += 1
            p *= 2
            if cnt % 2:
                begin += p / 2 + p * (n - 1)
            else:
                begin -= p / 2 + p * (n - 1)
        return begin