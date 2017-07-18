# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 16:28:55
# @Last Modified time: 2016-10-19 16:28:58
# @FileName: 415.py


class Solution(object):

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        max_len = max(len(num1), len(num2))
        num = [0] * (max_len + 1)
        for i in range(max_len):
            if i >= len(num1):
                num[i] += ord(num2[i]) - ord('0')
            elif i >= len(num2):
                num[i] += ord(num1[i]) - ord('0')
            else:
                num[i] += ord(num1[i]) + ord(num2[i]) - 2 * ord('0')
            if num[i] >= 10:
                num[i + 1] += num[i] / 10
                num[i] = num[i] % 10
        if num[max_len] == 0:
            num.pop()
        return ''.join([str(x) for x in num[::-1]])
