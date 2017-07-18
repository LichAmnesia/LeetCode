# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-15 23:43:05
# @Last Modified time: 2016-09-15 23:51:00
# @FileName: 13.py


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        while s:
            if len(s) == 1 or val[s[0]] >= val[s[1]]:
                res += val[s[0]]
                s = s[1:]
            else:
                res += val[s[1]] - val[s[0]]
                s = s[2:]
        return res