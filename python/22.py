# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 13:25:53
# @Last Modified time: 2016-10-01 13:42:02
# @FileName: 22.py


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []
        def dfs(l, r, s, n):
            if len(s) == 2 * n:
                ans.push(s)
                return 
            if l < n:
                dfs(l + 1, r, s + '(', n)
            if l > r:
                dfs(l, r + 1, s + ')', n)

        dfs(0, 0, '', n)
        return ans