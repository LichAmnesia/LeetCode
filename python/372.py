# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 18:14:45
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-02 18:17:43


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        power = a
        ans = 1
        for n in b[::-1]:
            ans = (ans * (power ** n)% 1337) % 1337
            power = (power ** 10) % 1337

        return ans