# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-28 13:42:23
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-28 14:41:07
# @Email: shen.huang@colorado.edu


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1: return len(word2)
        if not word2: return len(word1)
        
        dp = [[0] * (len(word2) + 1) for x in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[len(word1)][len(word2)]