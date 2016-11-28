# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-11-28 14:40:56
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-11-28 14:41:04
# @Email: shen.huang@colorado.edu

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        try:
            complex(s)
        except:
            return False
        return True