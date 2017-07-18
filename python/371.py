# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-16 00:34:11
# @Last Modified time: 2016-09-16 00:46:06
# @FileName: 371.py


class Solution(object):
    def add(self, a, b, n):
        if n > 32:
            return a
        return a if b == 0 else self.add(a ^ b, (a & b) << 1, n + 1)

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ans = self.add(a, b, 1)
        return ans if ans & 0x80000000 else ans & 0x3fffffff 
        
