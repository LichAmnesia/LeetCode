# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 01:32:19
# @Last Modified time: 2016-10-06 01:36:26
# @FileName: 89.py


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(1, n + 1):
            tmp = []
            for j in res:
                tmp.append(j + 2 ** (i - 1))
            tmp = tmp.reverse()
            res += tmp
        return res