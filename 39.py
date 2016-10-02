# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 11:49:57
# @Last Modified time: 2016-10-02 11:57:20
# @FileName: 39.py


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        res = []

        def dfs(minnum, remain):
            if remain == 0:
                ans.append([x for x in res])
            for i in range(minnum, len(candidates)):
                if candidates[i] <= remain:
                    res.append(candidates[i])
                    dfs(i, remain - candidates[i])
                    res.pop()
                

        dfs(0, target)
        return ans