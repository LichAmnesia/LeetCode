# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 17:13:52
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-06 17:34:23


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        max_len = 0
        for first in range(len(s) - k + 1):
            last = first
            count = [0 for x in range(30)]
            mask = 0
            max_last = first
            for last in range(first, len(s)):
                i = ord(s[last]) - ord('a')
                count[i] += 1
                num = min([x for x in count if x != 0])
                if num >= k:
                    max_len = max(max_len, last - first + 1)
                    max_last = last
                # print mask    
            if max_len > len(s) - first:
                break
            first = max_last + 1
        return max_len