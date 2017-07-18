# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-16 00:05:40
# @Last Modified time: 2016-09-16 00:10:08
# @FileName: 387.py


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1:
            return -1
        m = {}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = i
            else:
                m[s[i]] = -1
        tmp = sorted(m.values())
        for i in tmp:
            if i != -1:
                return i
        return -1