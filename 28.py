# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 15:24:20
# @Last Modified time: 2016-10-04 23:19:49
# @FileName: 28.py


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < 1 and len(needle) < 1:
            return 0
        elif len(needle) < 1:
            return 0
        elif len(haystack) < 1:
            return -1
        j = -1
        match = [-1 for x in range(len(needle))]
        match[0] = -1
        for i in range(1, len(needle)):
            while j != -1 and needle[j + 1] != needle[i]:
                j = match[j]
            if needle[j + 1] == needle[i]:
                j += 1
            match[i] = j
        j = -1
        for i in range(0, len(haystack)):
            while j != -1 and needle[j + 1] != haystack[i]:
                j = match[j]
            if needle[j + 1] == haystack[i]:
                j += 1
            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1