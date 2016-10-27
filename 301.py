# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-25 12:26:20
# @Last Modified time: 2016-10-25 12:28:05
# @FileName: 301.py


class Solution(object):

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def dfs(s):
            m = calc(s)
            if m == 0:
                return [s]
            ans = []
            for i in range(len(s)):
                if s[i] in ('(', ')'):
                    new_s = s[:i] + s[i + 1:]
                    if new_s not in vis and calc(new_s) < m:
                        vis.add(new_s)
                        ans.extend(dfs(new_s))
            return ans

        def calc(s):
            a, b = 0, 0
            for c in s:
                a += {'(': 1, ')': -1}.get(c, 0)
                b += a < 0
                a = max(a, 0)
            return a + b

        vis = set([s])
        return dfs(s)
