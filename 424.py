# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-15 22:49:52
# @Last Modified time: 2016-10-15 22:51:16
# @FileName: 424.py


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        for i in range(0, 26):
            c = chr(ord('A') + i)
            begin, end = 0, 0
            num_change = 0
            while end < len(s):
                if num_change < k or s[end] == c:
                    if s[end] != c:
                        num_change += 1
                    end += 1
                    res = max(end - begin, res)
                else:
                    if s[begin] != c:
                        num_change -= 1
                    begin += 1
        return res