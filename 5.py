# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-09 10:35:42
# @Last Modified time: 2016-09-09 14:36:47
# @FileName: 5.py
# This is a Manacher algorithm for solving longest palindromic substring
# Algorihm website https://segmentfault.com/a/1190000003914228


class Solution(object):
    def longestPalindrome(self, s="abcdeedcba"):
        """
        :type s: str
        :rtype: str
        """
        t = s
        s = '#'.join(s)
        s = '#' + s + '#'
        maxRight = 0
        pos = 0
        maxLen = 0
        pair = [-1 for i in range(len(s))]
        for i in range(len(s)):
            if i < maxRight:
                pair[i] = min(maxRight - i, pair[2 * pos - i])
            else:
                pair[i] = 1
            while i - pair[i] >= 0 and i + pair[i] < len(s) and s[i - pair[i]] == s[i + pair[i]]:
                pair[i] += 1
                if maxRight < pair[i] + i:
                    maxRight = pair[i] + i
                    pos = i
                if pair[i] > maxLen:
                    maxLen = pair[i]
                    ans = t[(i - maxLen + 1) / 2: (i + maxLen - 1) / 2]
        return ans


a = Solution()
a.longestPalindrome()
