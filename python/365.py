# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-14 16:02:20
# @Last Modified time: 2016-10-14 16:07:32
# @FileName: 365.py


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0: return True
        if x == 0 or y == 0: return x + y == z
        if z > x + y: return False
        if z % self.gcd(x, y) == 0:
            return True
        return False
    
    def gcd(self, a, b):
        if b == 0: return a
        return self.gcd(b, a % b)