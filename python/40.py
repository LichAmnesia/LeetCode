# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 17:48:40
# @Last Modified time: 2016-10-07 18:10:52
# @FileName: 40.py


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        res = []
        candidates = sorted(candidates)
        def dfs(minnum, remain):
            if remain == 0 and res not in ans:

                ans.append([x for x in res])
            for i in range(minnum, len(candidates)):
                if candidates[i] <= remain:
                    res.append(candidates[i])
                    dfs(i + 1, remain - candidates[i])
                    res.pop()
                

        dfs(0, target)
        return ans