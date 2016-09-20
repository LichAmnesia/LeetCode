# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 23:25:19
# @Last Modified time: 2016-09-19 10:52:32
# @FileName: 342.py


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        d = math.log10(num) / math.log10(4)
        return d.is_integer()