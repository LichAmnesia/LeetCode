# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-20 16:50:08
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-20 17:12:29



class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        mask = 0x7ffffff
        if len(s) < 10:
            return []
        dic = {}
        cur = 0
        i = 0
        while i < 9:
            cur = ((cur & mask) << 3) | (ord(s[i]) & 7)
            # cur &= mask
            i = i + 1
        res = []
        while i < len(s):
            cur = ((cur & mask) << 3) | (ord(s[i]) & 7)
            # cur &= mask
            val = dic.get(cur)
            # print cur,val,i, len(s)
            if val:
                # print val
                if val == 1:
                    res.append(s[i - 9: i + 1])
                dic[cur] += 1
            else:
                dic[cur] = 1
                
        
            i += 1
        return res