# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-18 16:45:45
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-18 16:45:46
# @Email: shen.huang@colorado.edu


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        cnt = 0
        loc = 0
        for w in abbr:
            if w.isdigit():
                if w == '0' and cnt == 0:
                    return False
                cnt = cnt * 10 + int(w) 
            else:
                loc = loc + cnt
                if loc >= len(word) or word[loc] != w:
                    return False
                cnt = 0
                loc += 1
        return loc + cnt == len(word)
        