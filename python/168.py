# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-29 02:04:15
# @Last Modified time: 2016-09-29 02:30:06
# @FileName: 168.py


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        while n:
            n -= 1
            s += unichr(65 + n % 26)
            n /= 26
        return s[::-1]