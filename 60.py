# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-14 16:26:03
# @Last Modified time: 2016-10-14 16:29:06
# @FileName: 60.py


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        r = ''; fac = [1]*(n+1); s = []
        for i in xrange(1, n+1):
            fac[i] = i*fac[i-1]
            s.append(i)
        for i in xrange(n, 0, -1):
            ind = (k-1)/fac[i-1]
            r += str(s[ind])
            del s[ind]
            k %= fac[i-1]
        return r