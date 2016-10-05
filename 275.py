# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 17:38:23
# @Last Modified time: 2016-10-04 17:44:56
# @FileName: 275.py


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = 0
        r = len(citations) - 1
        while l <= r:
            mid = (l + r) / 2
            if (citations[mid] >= len(citations) - mid):
                r = mid - 1
            else:
                l = mid + 1
        return len(citations) - l