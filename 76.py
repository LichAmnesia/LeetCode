# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-25 12:14:21
# @Last Modified time: 2016-10-25 12:14:22
# @FileName: 76.py


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) < 1 or len(s) < 1:
            return ""
        need_find = collections.Counter(t) 
        has_find = collections.Counter(t) 
        for i in has_find:
            has_find[i] = 0
        begin = 0
        end = 0
        ans = ""
        has_find[s[end]] += 1
        while begin <= end and begin < len(s):
            for i in need_find:
                while has_find[i] < need_find[i]:
                    if end == len(s) - 1:
                        return ans
                    else:
                        end += 1
                        has_find[s[end]] += 1
            if len(ans) == 0 or len(ans) > end - begin + 1:
                ans = s[begin: end + 1]
            
            while has_find[s[begin]] == need_find[s[begin]]:
                if end == len(s) - 1:
                    return ans
                else:
                    end += 1
                    has_find[s[end]] += 1
            while has_find[s[begin]] > need_find[s[begin]]:
                has_find[s[begin]] -= 1
                begin += 1
            if len(ans) == 0 or len(ans) > end - begin + 1:
                ans = s[begin: end + 1]
                
        return ans   
            