# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 11:57:27
# @Last Modified time: 2016-10-02 14:11:20
# @FileName: 77.py
# https://discuss.leetcode.com/topic/56916/recursive-python-solutions-beating-100
# 这是为什么呢，为什么可以剪枝

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        ans = []
        res = []

        def dfs(mini, k, dep):
            if dep == k:
                ans.append([x for x in res])
                return
            if len(res) > k:
                return
            for i in range(mini, n + 1 - (k - dep - 1)):
                res.append(i)
                dfs(i + 1, k, dep + 1)
                res.pop()

        dfs(1, k, 0)
        return ans