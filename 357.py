# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 17:04:39
# @Last Modified time: 2016-09-24 17:16:20
# @FileName: 357.py


class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solve(n, i):
            ans = 1
            for j in range(n, n - i, -1):
                ans *= j
            return ans

        if n == 0:
            return 1
        res = 10
        for i in range(2, n + 1):
            if i >= 10:
                return res

            res += 9 * solve(9, i - 1)
        return res
