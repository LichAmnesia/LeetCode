# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 15:33:21
# @Last Modified time: 2016-09-24 15:41:24
# @FileName: 204.py


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        vec = [True for x in range(n + 2)]
        for i in range(2, int(math.sqrt(n) + 1)):
            if vec[i]:
                for j in range(i * i, n, i):
                    vec[j] = False
        for i in range(2, n):
            ans += 1 if vec[i] else 0
        return ans
