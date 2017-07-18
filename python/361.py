# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 09:46:59
# @Last Modified time: 2016-11-17 10:02:53
# @FileName: 361.py

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n < 1: return 0
        m = len(grid[0])
        colH = [0] * m
        colR = 0
        ans = 0
        for i in range(0, n):
            for j in range(0, m):
                if not i or grid[i - 1][j] == 'W':
                    colH[j] = 0
                    for k in range(i, n):
                        if grid[k][j] == 'W': break
                        colH[j] += 1 if grid[k][j] == 'E' else 0
                if not j or grid[i][j - 1] == 'W':
                    colR = 0
                    for k in range(j, m):
                        if grid[i][k] == 'W': break
                        colR += 1 if grid[i][k] == 'E' else 0
                
                # print i, j, colH[j], colR
                if grid[i][j] == '0':
                    ans = max(colH[j] + colR, ans)
        return ans
                        