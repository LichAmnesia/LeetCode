# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-23 18:30:48
# @Last Modified time: 2016-10-23 19:12:26
# @FileName: 10.py


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = [[False] * (n + 1) for x in range(m + 1)]
        for i in range(n + 1):
            dp[i][0] = False
        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = j > 1 and p[j - 1] == '*' and dp[0][j - 2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j -
                                         1] and (p[j - 1] == s[i - 1] or '.' == p[j - 1])
                else:
                    dp[i][j] = dp[i][
                        j - 2] or ((s[i - 1] == p[j - 2] or '.' == p[j - 2]) and dp[i - 1][j])

        return dp[n][m]
