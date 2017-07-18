# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-28 17:00:56
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-28 17:00:58


class Solution(object):

    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x_list = []
        y_list = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x_list.append(i)
                    y_list.append(j)

        def getMid(num_list):
            num_list = sorted(num_list)
            sum = 0
            i, j = 0, len(num_list) - 1
            while i < j:
                sum += num_list[j] - num_list[i]
                i, j = i + 1, j - 1
            return sum

        if len(x_list) < 1:
            return 0
        return getMid(x_list) + getMid(y_list)
