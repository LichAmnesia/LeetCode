# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-18 11:20:32
# @Last Modified time: 2016-11-18 11:20:34
# @FileName: 320.py


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        n = len(word)
        if n < 1: return [""]
        times = 1 << n
        ans = []
        for i in range(times):
            res = ""
            cnt = 0
            for j in range(n):
                if (i >> j) & 1:
                   cnt += 1
                else:
                    if cnt != 0:
                        res += str(cnt)
                        cnt = 0
                    res += word[j]
            if cnt:
                res += str(cnt)
            ans.append(res)
        return ans