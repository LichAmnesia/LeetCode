# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 17:58:35
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-05 20:03:30


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        p = 0
        while m != n:
            m >>= 1
            n >>= 1
            p += 1
        return m << p