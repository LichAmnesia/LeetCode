# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-15 22:51:29
# @Last Modified time: 2016-10-15 23:05:32
# @FileName: 43.py

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        num = [0] * (len(num1) + len(num2) + 10)
        for i in range(len(num1)):
            for j in range(len(num2)):
                num[i + j] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
        for i in range(0, len(num1) + len(num2) + 10):
            if num[i] == 0 and i > len(num1) + len(num2):
                break
            if num[i] >= 10:
                    num[i + 1] += num[i] / 10
                    num[i] = num[i] % 10
        while len(num) > 1 and num[-1] == 0:
            num.pop()
        return ''.join([str(x) for x in num[::-1]])
        
