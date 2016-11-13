# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-13 11:14:03
# @Last Modified time: 2016-11-13 11:14:05
# @FileName: 157.py


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        for i in range(0, n, 4):
            tmp = [""] * 4
            len_ = read4(tmp)
            num = min(len_, n - i)
            buf[i:i + num] = tmp[:num]
            if len_ < 4: return min(i + len_, n)
        return n