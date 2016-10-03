# -*- coding: utf-8 -*-
# @Author: lich
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 18:03:32
# @Last Modified by:   lich
# @Last Modified time: 2016-10-02 18:13:08


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        stack = [1]
        ans = []
        while stack:
            tmp = stack.pop()
            ans.append(tmp)
            if tmp * 10 <= n:
                stack.append(tmp * 10)
            if tmp < n and tmp % 10 < 9:
                stack.append(tmp + 1)

        return ans