# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-02 00:05:48
# @Last Modified time: 2016-11-02 00:05:51
# @FileName: 188.py


class Solution(object):

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 1 or k < 1:
            return 0
        if 2 * k >= n:
            return self.noKLimit(prices)
        global_dp = [[0] * (k + 1) for x in range(n)]
        local_dp = [[0] * (k + 1) for x in range(n)]

        for i in range(1, n):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k + 1):
                local_dp[i][j] = max(
                    local_dp[i - 1][j] + diff, global_dp[i - 1][j - 1] + max(diff, 0))
                global_dp[i][j] = max(global_dp[i - 1][j], local_dp[i][j])
        return global_dp[n - 1][k]

    def noKLimit(self, prices):
        sum = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                sum += prices[i] - prices[i - 1]
        return sum
