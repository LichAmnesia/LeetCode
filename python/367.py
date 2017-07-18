# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 20:40:31
# @Last Modified time: 2016-10-01 20:45:42
# @FileName: 367.py


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 0
        while i * i < num:
            i += 1
            if long(i) * i > num:
                return False
            elif long(i) * i == num:
                return True
