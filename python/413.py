# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 20:28:43
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-19 20:28:45


class Solution(object):

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [0, 0]
        list_len = 1
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp.append(dp[-1] + list_len)
                list_len += 1
            else:
                dp.append(dp[-1])
                list_len = 1
        return dp[-1]
