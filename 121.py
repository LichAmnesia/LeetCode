# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 00:05:41
# @Last Modified time: 2016-09-20 00:15:06
# @FileName: 121.py


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 1:
            return 0
        dpMin = [0 for x in range(len(prices))]
        dpMax = [0 for x in range(len(prices))]
        res = 0
        dpMin[0] = prices[0]
        for i in range(1, len(prices)):
            dpMin[i] = min(dpMin[i - 1], prices[i])
        dpMax[len(prices) - 1] = prices[len(prices) - 1]
        for i in range(1, len(prices)):
            dpMax[len(prices) - i - 1] = max(dpMax[len(prices) - i], prices[len(prices) - i - 1])
        # print dpMax, dpMin
        for i in range(len(prices)):
            res = max(res, dpMax[i] - dpMin[i])
        return res
