# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 01:00:37
# @Last Modified time: 2016-10-19 01:01:21
# @FileName: 91.py


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1 or s[0] == '0':
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            dp[i] = dp[i - 1]
            if s[i - 1] == '0':
                if s[i - 2] in '12':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            elif s[i - 2] == '1' or s[i - 2] == '2' and s[i - 1] < '7':
                dp[i] += dp[i - 2]

        return dp[len(s)]
