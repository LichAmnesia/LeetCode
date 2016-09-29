# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-29 09:41:14
# @Last Modified time: 2016-09-29 10:19:59
# @FileName: 278.py


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l + r) / 2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l