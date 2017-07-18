# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-18 16:29:46
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-18 16:31:55
# @Email: shen.huang@colorado.edu
# 首先得到repeat数组，以及有多少type。
# 然后根据total字符串长度，如果小于6就添加max(要加长度，和所差type)
# 如果大于20，那么每次要进行删除几个，这个要贪心，从mod余数为0的开始。然后如果删到已经为20了，就开始change。
# 如果是小于20的那么直接算change的部分就行了。

class Solution(object):
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = len(s)
        repeat = []
        types = 0
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                if cnt >= 3:
                    repeat.append(cnt)
                cnt = 1
        if cnt >= 3:
            repeat.append(cnt)
        # print repeat
        for i in range(len(s)):
            if s[i] <= 'z' and s[i] >= 'a':
                types |= 1
            if s[i] >= 'A' and s[i] <= 'Z':
                types |= 2
            if s[i] >= '0' and s[i] <= '9':
                types |= 4
        if types == 7:
            types = 3
        elif types in [1, 2, 4]:
            types = 1
        else:
            types = 2
        
        if total < 6:
            return max(6 - total, 3 - types)
        
        deleteCnt = max(0, total - 20)
        
        heap = [(r % 3, r) for r in repeat]
        heapq.heapify(heap)
        
        while total > 20 and heap:
            mod, r = heapq.heappop(heap)
            delta = min(total - 20, mod + 1)
            total -= delta
            heapq.heappush(heap, (2, r - delta))
        
        changeCnt = sum([r / 3 for mod, r in heap])
        # print changeCnt, types, heap
        return deleteCnt + max(changeCnt, 3 - types)
            
