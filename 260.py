# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-23 17:03:31
# @Last Modified time: 2016-09-23 20:21:51
# @FileName: 260.py


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        one = set()
        two = set()
        for i in nums:
            if i not in one:
                one.add(i)
            else:
                two.add(i)
        ans = one - two
        return [x for x in ans]
