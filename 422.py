# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-10 23:57:46
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-10 23:57:46
# @Email: shen.huang@colorado.edu

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        n = len(words)
        m = len(words[0]) if n else 0
        if n != m:
            return False
        for x in range(n):
            len_s = len(words[x])
            c = 0
            for y in range(n):
                if len(words[y]) < x + 1:
                    break
                c += 1
            if c != len_s:
                return False
            for y in range(len_s):
                if words[x][y] != words[y][x]:
                    return False
        return True