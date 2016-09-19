# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-18 22:34:30
# @Last Modified time: 2016-09-18 22:35:20
# @FileName: 190.py


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        int('0b' + bin(n)[2::-1], 2)