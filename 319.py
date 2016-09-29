# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-29 00:03:04
# @Last Modified time: 2016-09-29 00:52:39
# @FileName: 319.py


class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        return int(math.sqrt(n))