# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 02:32:52
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 02:36:09
# https://discuss.leetcode.com/topic/25970/concise-python-solution-10-lines

class Solution(object):

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_letters = [], [], 0
        for w in words:
            if len(cur) + num_letters + len(w) > maxWidth:
                for i in range(maxWidth - num_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_letters = [], 0
            cur += [w]
            num_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
