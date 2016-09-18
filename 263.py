# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 16:01:20
# @Last Modified time: 2016-09-18 16:07:20
# @FileName: 263.py


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num <= 0:
            return False
        for i in 2, 3, 5:
            while num % i == 0:
                num /= i
        return num == 1