# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 16:42:47
# @Last Modified time: 2016-11-17 16:42:58
# @FileName: 293.py

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        s = list(s)
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                s[i] = s[i + 1] = '-'
                ans.append(''.join(s))
                s[i] = s[i + 1] = '+'
        return ans