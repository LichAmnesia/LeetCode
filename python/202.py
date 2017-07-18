# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-15 14:46:01
# @Last Modified time: 2016-09-15 14:52:01
# @FileName: 202.py


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = set()
        m.add(n)
        while n != 1:
            s = str(n)
            sum = 0
            for i in s:
                sum += int(i) * int(i)
            n = sum
            if n in m:
                return False
            m.add(n)
        return True
