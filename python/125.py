# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-24 15:38:47
# @Last Modified time: 2016-09-24 16:50:27
# @FileName: 125.py


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 1:
            return True
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        if len(s) < 1:
            return True
        s = s.lower()
        return s == s[::-1]