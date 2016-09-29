# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-29 00:44:28
# @Last Modified time: 2016-09-29 01:06:09
# @FileName: 165.py


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def encode(str):
            v = [long(s) for s in str.split('.')]
            while v and v[-1] == 0:# delete trailing zeros
                v.pop()
            return v

        return cmp(encode(version1), encode(version2))
