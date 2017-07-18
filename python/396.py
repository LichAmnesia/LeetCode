# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 22:53:22
# @Last Modified time: 2016-09-18 22:58:43
# @FileName: 396.py


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sum_ = 0
        sum_of_all = 0
        for i in range(len(A)):
            sum_ += A[i]
            sum_of_all += A[i] * i
        res = sum_of_all
        for i in range(len(A)):
            tmp = len(A)
            sum_of_all = sum_of_all - tmp * A[len(A) - 1 - i] + sum_
            res = max(res, sum_of_all)
        return res