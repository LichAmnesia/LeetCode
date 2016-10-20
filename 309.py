# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 21:08:49
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-19 21:08:52


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 1:
            return 0
        dp = [[0, 0] for x in range(n + 1)]
        dp[0][0], dp[0][1] = 0, - prices[0]
        # print dp
        for i in range(1, n):
            # print i
            dp[i][0] = max(dp[i - 1][0] + prices[i] -
                           prices[i - 1], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1] - prices[i] + prices[i - 1],
                           dp[i - 2][0] - prices[i] if i >= 2 else None)
        # print dp
        return max(dp)[0]
