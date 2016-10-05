# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-04 22:44:24
# @Last Modified time: 2016-10-04 23:01:15
# @FileName: 405.py


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        he = '0123456789abcdef'
        ans = []
        if num < 0:
            num += 0x100000000
        while num:
            ans.append(he[num % 16])
            num /= 16
        return ''.join(ans)
