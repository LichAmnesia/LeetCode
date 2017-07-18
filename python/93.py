# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-14 15:49:23
# @Last Modified time: 2016-10-14 16:02:03
# @FileName: 93.py


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        if len(s) > 20: return []
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) - 1):
                for k in range(j + 1, len(s) - 1):
                    if self.isIp(s[:i + 1]) and self.isIp(s[i + 1: j + 1]) and self.isIp(s[j + 1: k + 1]) and self.isIp(s[k + 1:]):
                        ans.append('.'.join([s[:i + 1],s[i + 1: j + 1],s[j + 1: k + 1],s[k + 1:]]))
        
        return ans
    
    def isIp(self, s):
        if len(s) > 1 and s[0] == '0': return False
        if len(s) > 3: return False
        s = int(s)
        if s >= 256: return False
        return True