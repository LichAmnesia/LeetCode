# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 11:26:15
# @Last Modified time: 2016-09-22 11:51:05
# @FileName: 205.py


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return all(map({}.setdefault, a, b) == list(b) for a, b in ((s, t), (t, s)))
