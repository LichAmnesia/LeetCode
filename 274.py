# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 17:31:17
# @Last Modified time: 2016-10-04 17:44:57
# @FileName: 274.py


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        hindex = -1
        for i in range(len(citations)):
            if citations[i] == len(citations) - i:
                hindex = i
        return hindex