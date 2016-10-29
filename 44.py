# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-28 16:33:58
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-28 16:34:03
# MLE

class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ns = len(s)
        np = len(p)
        if not ns and not np:
            return True
        dp = [[False] * (np + 1) for x in range(ns + 1)]
        # print dp
        dp[0][0] = True
        for i in range(1, np + 1):
            dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'
        for i in range(1, ns + 1):
            dp[i][0] = False
        for i in range(1, ns + 1):
            for j in range(1, np + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[ns][np]
