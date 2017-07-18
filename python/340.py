# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 10:44:26
# @Last Modified time: 2016-11-17 10:44:26
# @FileName: 340.py


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic = collections.defaultdict()
        left = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
            while len(dic) > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0: del dic[s[left]]
                left += 1
            ans = max(ans, i - left + 1)
        return ans
            
        