# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-16 01:17:04
# @Last Modified time: 2016-09-16 01:21:40
# @FileName: 242.py


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ms, mt = {}, {}
        for i in range(len(s)):
            if s[i] in ms:
                ms[s[i]] += 1
            else:
                ms[s[i]] = 1
        for i in range(len(t)):
            if t[i] in mt:
                mt[t[i]] += 1
            else:
                mt[t[i]] = 1
        for keys in ms.keys():
            if keys not in mt or ms[keys] != mt[keys]:
                return False
        for keys in mt.keys():
            if keys not in ms or ms[keys] != mt[keys]:
                return False
        return True
