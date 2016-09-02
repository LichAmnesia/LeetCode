# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-02 01:53:36
# @Last Modified time: 2016-09-02 02:02:58
# @FileName: 7.py

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if len(str(x)) == 1:
        #     return x
        if x < 0:
            if int('-'+str(x)[1:][::-1]) < - 2 ** 31:
                return 0
            return int('-'+str(x)[1:][::-1]) 
        if int(str(x)[::-1]) > 2 ** 31-1:
            return 0

        return int(str(x)[::-1])