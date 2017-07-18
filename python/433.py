# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-26 19:08:56
# @Last Modified time: 2016-10-26 19:08:57
# @FileName: 433.py


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        
        def getNum(gen):
            table = {v: i for i, v in enumerate('AGCT')}
            return sum([table[v] * (1 << (i * 2)) for i, v in enumerate(gen)])
            
        bank = set(map(getNum, bank))
        start = getNum(start)
        end = getNum(end)
        queue = [(start, 0)]
        vis = set([start])
        while queue:
            now, step = queue.pop(0)
            if now == end:
                return step
            for i in range(8):
                for j in range(4):
                    new_str = now ^ (j << (2 * i))
                    if new_str in bank and new_str not in vis:
                        vis.add(new_str)
                        queue.append((new_str, step + 1))
        return -1