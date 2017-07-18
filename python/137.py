# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-30 20:53:49
# @Last Modified time: 2016-09-30 20:59:49
# @FileName: 137.py


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = set(nums)
        # a = sum(s) * 3 - sum(nums)
        # return a / 2
        neg = 0
        res = 0
        for i in range(32):
            sum = 0
            for num in nums:
                if num < 0:
                    neg += 1
                    num *= -1
                sum += 1 & (num >> i)
            res += (sum % 3) << 1
        if neg % 3:
            res *= -1
        return res