# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-20 00:39:00
# @Last Modified time: 2016-10-20 00:47:01
# @FileName: 134.py


class Solution(object):

    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)
        i = 0
        while i < n:
            now = gas[i]
            j = 0
            while j < n:
                pos = (i + j + n) % n
                # print now, cost[pos]
                if now >= cost[pos]:
                    now = now - cost[pos] + gas[(pos + 1) % n]
                else:
                    i = max(pos, i)
                    break
                j += 1
            # print i, j

            if j == n:
                return i
            i += 1
        return -1
