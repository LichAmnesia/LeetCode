# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-17 09:09:32
# @Last Modified time: 2016-09-17 09:19:10
# @FileName: 389.py


class Solution(object):

    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(lambda x, y: x ^ y, map(ord, s + t)))
