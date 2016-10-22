# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:55:38
# @Last Modified time: 2016-10-21 22:55:43
# @FileName: 423.py


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = collections.Counter(s)
        nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        num_list = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        num_count = [collections.Counter(nums[i]) for i in num_list]
        ans = []
        # print cnts
        # print num_count
        for idx, val in enumerate(num_count):
            t = min(cnts[c] / val[c] for c in val)
            ans.append(t)
            for c in val:
                cnts[c] -= t * val[c]
        return ''.join(sorted([str(num_list[idx]) * val for idx, val in enumerate(ans)]))
        
                