# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 19:44:59
# @Last Modified time: 2016-09-20 20:14:14
# @FileName: 119.py


class Solution(object):

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        # rowIndex += 1
        # dp = [[0 for x in range(rowIndex)], [0 for x in range(rowIndex)]]
        # dp[0][0] = 1
        # pre, now = 0, 1
        # for i in range(1, rowIndex):
        #     dp[now][0] = 1
        #     for j in range(1, i):
        #         dp[now][j] = dp[pre][j - 1] + dp[pre][j]
        #     dp[now][i] = 1
        #     pre, now = now, pre
        # return dp[pre]
        result = [0] * (rowIndex + 1)
        rowIndex += 1
        result[0] = 1
        for i in range(1, rowIndex):
            for j in reversed(range(1, i + 1)):
                result[j] += result[j - 1]
        return result

