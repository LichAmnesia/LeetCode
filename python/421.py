# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-11 00:31:35
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-11 00:31:43
# @Email: shen.huang@colorado.edu
# https://discuss.leetcode.com/topic/63213/java-o-n-solution-using-bit-manipulation-and-hashmap/8

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = masks = 0
        for i in range(32, -1, -1):
            masks += 1 << i
            pre_set = set([n & masks for n in nums])
            tmp = ans | 1 << i
            for item in pre_set:
                if tmp ^ item in pre_set:
                    ans = tmp
                    break
        return ans