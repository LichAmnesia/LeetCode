# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-01 23:16:03
# @Last Modified time: 2016-10-01 23:21:45
# @FileName: 46.py


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def generate(num):
            if not num:
                yield []
            for i in num:
                for permutation in generate([x for x in num if x != i]):
                    yield [i] + permutation

        return [x for x in generate(nums)]