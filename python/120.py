# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-05 17:09:10
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-05 17:22:38


class Solution(object):

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = [[sys.maxint for x in range(len(triangle[i]))]
              for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(0, len(triangle) - 1):
            for j in range(len(triangle[i])):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1],
                                       dp[i][j] + triangle[i + 1][j + 1])
        n = len(triangle)
        ans = sys.maxint
        for i in range(len(triangle[n - 1])):
            ans = min(ans, dp[n - 1][i])
        return ans
