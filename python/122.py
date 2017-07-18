# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 16:53:47
# @Last Modified time: 2016-09-24 16:56:14
# @FileName: 122.py


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i]:
                ans += prices[i] - prices[i - 1]
        return ans