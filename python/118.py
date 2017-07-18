# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 01:41:43
# @Last Modified time: 2016-09-20 01:50:57
# @FileName: 118.py


class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return []
        dp = [[] for x in range(numRows)]
        dp[0].append(1)
        for i in range(1, numRows):
            dp[i].append(1)
            for j in range(1, i):
                dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
            dp[i].append(1)
        return dp
