# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 23:58:37
# @Last Modified time: 2016-10-06 00:04:32
# @FileName: 375.py


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        dp = [[0] * (n + 1) for x in range(n + 1)]

        def dfs(dp, l, r):
            if l >= r:
                return 0
            if dp[l][r] == 0:
                dp[l][r] = min(i + max(dfs(dp, l, i - 1), dfs(dp, i + 1, r)) for i in range(l, r + 1))
            return dp[l][r]

        return dfs(dp, 1, n)