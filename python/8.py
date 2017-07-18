# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-02 00:10:55
# @Last Modified time: 2016-09-02 01:49:05
# @FileName: 8.py

import sys
class Solution(object):
    def myAtoi(self, stri):
        """
        :type str: str
        :rtype: int
        """
        if len(stri) < 1:
            return 0
        nowstr = ''
        for x in stri.split(' '):
            if x != '':
                nowstr = x
                break
        flag = 1
        if nowstr[0] == '-':
            flag = -1
            nowstr = nowstr[1:]
        elif nowstr[0] == '+':
            flag = 1
            nowstr = nowstr[1:]
        elif not ('0' <= nowstr[0] and nowstr[0] <= '9'):
            return 0

        res_num = long(0)
        for i in nowstr:
            if '0' <= i and i <= '9':
                res_num *= 10
                res_num += long(i)
            else:
                if res_num * flag >= 2147483648:
                    return 2147483647
                if res_num * flag <= -2147483649:
                    return -2147483648
                return res_num * flag
        if res_num * flag >= 2147483648:
            return 2147483647
        if res_num * flag <= -2147483649:
            return -2147483648
        return res_num * flag
     


my = Solution()
print my.myAtoi("2147483648")

