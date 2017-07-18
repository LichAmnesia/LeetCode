# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 14:11:34
# @Last Modified time: 2016-09-20 14:30:58
# @FileName: 14.py


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ""
        minLen = min(map(lambda x: len(x), strs))
        for j in range(minLen):
            tmp = strs[0][j]
            for i in range(1, len(strs)):
                if strs[i][j] != tmp:
                    return strs[0][:j]
        return strs[0][:minLen]
