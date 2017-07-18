# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 23:20:43
# @Last Modified time: 2016-09-18 23:23:53
# @FileName: 58.py


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if len(s) < 1:
            return 0
        s = s[-1]
        return len(s)
