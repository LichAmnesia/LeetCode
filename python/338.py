# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 17:51:09
# @Last Modified time: 2016-09-24 19:12:40
# @FileName: 338.py


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        fac = [0 for x in range(num + 1)]
        i = 1 
        while i <= num:
            fac[i] = 1
            i *= 2
        base = 2
        for i in range(2, num + 1):
            if fac[i] == 0:
                fac[i] = fac[i - base] + 1
            else:
                base = i
        return fac