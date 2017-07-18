# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 01:24:35
# @Last Modified time: 2016-10-04 01:37:23
# @FileName: 200.py


class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        maps = [[] for x in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maps[i].append(int(grid[i][j]))
        dic = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def dfs(x, y):
            maps[x][y] = 0
            for i in range(4):
                x, y = x + dic[i][0], y + dic[i][1]

                if x >= 0 and x < len(maps) and y >= 0 and y < len(maps[0]) and maps[x][y] == 1:
                    dfs(x, y)
                x, y = x - dic[i][0], y - dic[i][1]

        ans = 0
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == 1:
                    ans += 1
                    dfs(i, j)
        return ans
