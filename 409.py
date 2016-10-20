# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 19:56:38
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-19 19:56:40


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        flag = False
        ans = 0
        for key, value in dic.iteritems():
            if value & 1:
                flag = True
            if value / 2 > 0:
                ans += value / 2 * 2
        if flag:
            ans += 1
        return ans
