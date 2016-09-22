# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-22 12:16:53
# @Last Modified time: 2016-09-22 12:22:42
# @FileName: 374.py


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        mid = (1 + n) / 2
        l = 1
        r = n
        while l < r:
            # print mid
            if guess(mid) < 0:
                r = mid - 1
            elif guess(mid) > 0:
                l = mid + 1
            else:
                return mid
            mid = (l + r) / 2
        return mid