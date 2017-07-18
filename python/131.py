# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 14:33:59
# @Last Modified time: 2016-10-07 14:52:08
# @FileName: 131.py



class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ans = []

        def dfs(s, res):
            if not s:
                res = list(res)
                self.ans.append(res)
            for i in range(len(s)):
                if self.isPalidrome(s[:i + 1]):
                    res.append(s[:i + 1])
                    dfs(s[i + 1:], res)
                    res.pop()

        dfs(s, [])
        return self.ans

    def isPalidrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True