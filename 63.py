# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 18:10:55
# @Last Modified time: 2016-10-07 18:10:56
# @FileName: 63.py


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        if n < 1: return 0
        m = len(obstacleGrid[0])
        dp = [[0 for x in range(m)] for y in range(n)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(1, n):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, m):
            if obstacleGrid[0][i] != 1:
                dp[0][i] = dp[0][i - 1]
        # print dp
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] += dp[i][j - 1] + dp[i - 1][j]
        return dp[n - 1][m - 1]