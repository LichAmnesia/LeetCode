# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 02:28:40
# @Last Modified time: 2016-09-20 02:49:32
# @FileName: 290.py


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m1, m2 = {}, {}
        for i in range(len(pattern)):
            m1[pattern[i]] = -1
        str = str.split()
        for i in range(len(str)):
            m2[str[i]] = -1
        if len(pattern) != len(str):
            return False
        for i, j in enumerate(pattern):
            if m1[pattern[j]] != m2[str[i]]:
                return False
            m1[pattern[j]] = i
            m2[str[i]] = i
        return True
