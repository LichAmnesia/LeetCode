# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-26 20:27:21
# @Last Modified time: 2016-10-26 20:27:56
# @FileName: 140.py


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """

        if not s or not wordDict or not self.isBreak(s, wordDict):
            return []
        # print "ss"
        dp = [[] for i in range(len(s) + 1)]
        dp[0].append('')
        for i in range(0, len(s)):
            for j in range(1, i + 2):
                if s[i - j + 1: i + 1] in wordDict:
                    if i - j + 1 != 0 and dp[i - j + 1]:
                        dp[i + 1] += [each + ' ' + s[i - j + 1: i + 1]
                                      for each in dp[i - j + 1]]
                    elif i - j + 1 == 0:
                        dp[i + 1].append(s[i - j + 1: i + 1])
        return dp[-1]

    def isBreak(self, s, wordDict):
        if not s or not wordDict:
            return False
        dp = [0 for x in range(len(s) + 1)]
        dp[0] = 1
        for i in range(0, len(s)):
            for j in range(1, i + 2):
                if s[i - j + 1: i + 1] in wordDict:
                    dp[i + 1] += dp[i - j + 1]
            # print dp[i + 1]
        return dp[-1] > 0
