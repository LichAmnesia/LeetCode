# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-20 01:36:11
# @Last Modified time: 2016-09-20 02:13:18
# @FileName: 66.py


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) < 1:
            return [1]
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
            if i < 0:
                return [1] + digits