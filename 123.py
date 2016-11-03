# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-01 23:40:01
# @Last Modified time: 2016-11-01 23:40:01
# @FileName: 123.py


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 1:
            return 0
        dp = [0] * n
        dp[0] = 0
        min_price = prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], prices[i] - min_price)
            min_price = min(prices[i], min_price)

        max_profit = 0
        max_price = prices[n - 1]
        ans = 0
        for i in range(n - 1, -1, -1):
            ans = max(ans, max_profit + dp[i])
            max_profit = max(max_profit, max_price - prices[i])
            max_price = max(max_price, prices[i])
        return ans
