# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 10:24:03
# @Last Modified time: 2016-10-07 10:41:06
# @FileName: 322.py



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [sys.maxint for x in range(amount + 1)]
        dp[0] = 0
        coins = sorted(coins, reverse=1)
        for coin in coins:
            for i in range(amount):
                if dp[i] != sys.maxint and i + coin <= amount:
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin])
        return dp[amount] if dp[amount] != sys.maxint else -1
