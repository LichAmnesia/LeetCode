# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 01:53:44
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 01:53:46


class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        max_len = 1
        data = {}
        for n in dic:
            if n in data:
                continue
            l, r = n - 1, n + 1
            cnt = 1
            data[n] = 1
            while l in dic or r in dic:
                if l in dic:
                    cnt += 1
                    data[l] = 1
                    l = l - 1
                if r in dic:
                    cnt += 1
                    data[r] = 1
                    r = r + 1
                max_len = max(max_len, cnt)
        return max_len
