# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:54:35
# @Last Modified time: 2016-10-21 22:54:53
# @FileName: 393.py

class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        
        masks = [0x0, 0x80, 0xE0, 0xF0, 0xF8]
        bits = [0x0, 0x0, 0xC0, 0xE0, 0xF0]
        while data:
            for i in xrange(4, -1, -1):
                if i == 0:
                    return False
                if data[0] & masks[i] == bits[i]:
                    if len(data) < i:
                        return False
                    for j in range(1, i):
                        if data[j] & 0xC0 != 0x80:
                            return False
                    data = data[i:]
                    break
        return True