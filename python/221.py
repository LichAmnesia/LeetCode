# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 02:03:50
# @Last Modified time: 2016-10-07 02:12:30
# @FileName: 221.py


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) < 1:
            return 0

        dp = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        ans = 0
        for i in range(len(matrix[0])):
            dp[0][i] = ord(matrix[0][i]) - ord('0')
            ans = max(dp[0][i], ans)
        for i in range(len(matrix)):
            dp[i][0] = ord(matrix[i][0]) - ord('0')
            ans = max(dp[i][0], ans)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                dp[i][j] = min(min(dp[i-1][j], dp[i-1][j-1]), dp[i][j-1]) + 1 if matrix[i][j] == '1' else 0
                ans = max(dp[i][j], ans)
        return ans * ans