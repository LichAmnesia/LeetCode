# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 16:50:39
# @Last Modified time: 2016-09-24 16:56:29
# @FileName: 343.py


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        dp = [0 for x in range(n + 4)]
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for i in range(5, n + 1):
            dp[i] = dp[i - 3] * 3
        return dp[n]