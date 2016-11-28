# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-27 18:53:01
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-27 19:23:05
# @Email: alwaysxiaop@gmail.com
# need to use deep copy to get the answer
# use bfs.

import copy

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        val = 0
        res = sys.maxint
        sum_list = copy.deepcopy(grid)
        dirc = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        for i in range(len(grid)):
        	for j in range(len(grid[0])):
        		if grid[i][j] == 1:
        			res = sys.maxint
        			dist = copy.deepcopy(grid)
        			
        			q = collections.deque()
        			q.append((i, j))
        			while q:
        				x, y = q.popleft()
        				for k in range(0, 4):
        					dx, dy = x + dirc[k][0], y + dirc[k][1]
        				# 	print(dx, dy, len(grid), len(grid[0]))
        				# 	if dx >= 0 and dx < len(grid) and dy >= 0 and dy < len(grid[0]):
        				# 	    print(grid[dx][dy])
        					if dx >= 0 and dx < len(grid) and dy >= 0 and dy < len(grid[0]) and grid[dx][dy] == val:
        						grid[dx][dy] -= 1
        						dist[dx][dy] = dist[x][y] + 1
        						sum_list[dx][dy] += dist[dx][dy] - 1
        						q.append((dx, dy))
        						res = min(sum_list[dx][dy], res)
        # 			print(res)
        			val -= 1
        return -1 if res == sys.maxint else res