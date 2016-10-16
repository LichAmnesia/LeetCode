# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-15 23:06:11
# @Last Modified time: 2016-10-15 23:19:24
# @FileName: 306.py


class Solution(object):

    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """

        def dfs(start, pre1, pre2):
            if start == len(num):
                return True
            if len(pre1) > 1 and pre1[0] == "0":
                return False
            if len(pre2) > 1 and pre2[0] == "0":
                return False
            for i in range(start, len(num)):
                if num[start] == '0' and i != start:
                    continue
                if int(num[start: i + 1]) == int(pre1) + int(pre2) and dfs(i + 1, pre2, num[start: i + 1]):
                    return True
            return False

        for i in range(len(num) - 1):
            for j in range(i + 1, len(num) - 1):
                if dfs(j + 1, num[:i + 1], num[i + 1: j + 1]):
                    return True
        return False
