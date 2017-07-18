# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 22:26:28
# @Last Modified time: 2016-10-30 21:10:13
# @FileName: 67.py
# Wrong for one time

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = bin(int(a,2) + int(b,2))[2:]
        return res


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            return self.addBinary(b, a)
        
        a = map(int, a)[::-1]
        b = map(int, b)[::-1]
        b.append(0)
        for i in range(len(a)):
            b[i] = a[i] + b[i]
            if b[i] >= 2:
                tmp = b[i] / 2
                b[i + 1] += tmp
                b[i] = b[i] % 2
        
        
        for i in range(len(a), len(b)):
            if b[i] >= 2:
                b[i + 1] += b[i] / 2
                b[i] = b[i] % 2
        print b
        if b[-1] == 0:
            b.pop()
        return ''.join([str(x) for x in b])[::-1]