# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 17:23:13
# @Last Modified time: 2016-11-17 17:23:13
# @FileName: 249.py


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        n = len(strings)
        if n < 1: return []
        dic = collections.defaultdict(list)
        for i in range(n):
            if len(strings[i]) == 1:
                dic[(1)].append(strings[i])
            else:
                seq = (1,)
                for j in xrange(1, len(strings[i])):
                    d = ord(strings[i][j]) - ord(strings[i][j-1])
                    if d < 0: d += 26
                    seq += (d,)
                dic[seq].append(strings[i])
        return dic.values()