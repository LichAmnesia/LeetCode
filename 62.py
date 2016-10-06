# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 16:49:49
# @Last Modified time: 2016-10-05 17:00:11
# @FileName: 62.py



class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for x in range(n)] if y == 0 else [1 if x == 0 else 0 for x in range(n)] for y in range(m + 1)]
        # print dp
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += dp[i][j - 1] + dp[i - 1][j]
        return dp[m - 1][n - 1]