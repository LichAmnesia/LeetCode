# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 23:10:54
# @Last Modified time: 2016-10-01 23:16:05
# @FileName: 96.py


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {}
        def dfs(n):
            if n == 0:
                return 1
            sum = 0
            for i in range(1, n + 1):
                l = i - 1
                r = n - i
                if l not in memo:
                    memo[l] = dfs(l)
                if r not in memo:
                    memo[r] = dfs(r)
                sum += memo[l] * memo[r]
            return sum

        return dfs(n)