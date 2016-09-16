# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-16 01:09:47
# @Last Modified time: 2016-09-16 01:15:36
# @FileName: 171.py


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
            sum += (ord(s[i]) - ord('A') + 1) * 26**(len(s) - 1 - i) 
        return sum