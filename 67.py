# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 22:26:28
# @Last Modified time: 2016-09-18 22:34:25
# @FileName: 67.py


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = bin(int(a,2) + int(b,2))[2:]
        return res