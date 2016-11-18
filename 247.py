# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-18 11:04:46
# @Last Modified time: 2016-11-18 11:04:47
# @FileName: 247.py

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return [""]
        if n == 1: return ["0", "1", "8"]
        if n == 2: return ["11", "69", "88", "96"]
        a = ["0", "1", "8"]
        b = ["00", "11", "69", "88", "96"]
        cnt = 2
        for i in range(1, (n + 1) / 2):
            tmp = []
            cnt += 1
            for s in a:
                if cnt != n: tmp.append("0" + s + "0")
                tmp.append("1" + s + "1")
                tmp.append("6" + s + "9")
                tmp.append("9" + s + "6")
                tmp.append("8" + s + "8")
            a = tmp
            
            tmp = []
            cnt += 1
            for s in b:
                if cnt != n: tmp.append("0" + s + "0")
                tmp.append("1" + s + "1")
                tmp.append("6" + s + "9")
                tmp.append("9" + s + "6")
                tmp.append("8" + s + "8")
            b = tmp
        if n % 2 == 1:
            return a
        else:
            return b
                