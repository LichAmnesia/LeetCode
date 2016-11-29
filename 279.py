# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 00:23:16
# @Last Modified time: 2016-11-28 21:47:54
# @FileName: 279.py


class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]



class Solution(object):    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1000] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            dp[i] = min(dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)) + 1
            # for j in range(1, int(i ** 0.5) + 1):
            #     dp[i] = min(dp[i - j * j], dp[i])
            # dp[i] += 1
        return dp[n]