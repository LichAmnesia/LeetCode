# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 13:06:53
# @Last Modified time: 2016-10-01 13:15:26
# @FileName: 216.py


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        res = set()

        def dfs(minnum, k, remain):
            if remain == 0 and k == 0:
                ans.append([x for x in res])
            for i in range(minnum, min(remain + 1, 10)):
                if i not in res:
                    res.add(i)
                    dfs(i, k - 1, remain - i)
                    res.remove(i)

        dfs(1, k, n)
        return ans