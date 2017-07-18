# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-19 20:35:42
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-19 20:38:35


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < 1 or numRows == 1:
            return s
        rows = ["" for x in range(numRows)]
        i, go_right = -1, False
        for ch in s:
            i = i - 1 if go_right else i + 1
            rows[i] += ch
            go_right = True if i == numRows - 1 else False if i == 0 else go_right
        return ''.join(rows)
