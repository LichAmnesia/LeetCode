# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2016-12-22 15:03:06
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2016-12-22 15:03:08
# @Email: shen.huang@colorado.edu



class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        nums = sorted(envelopes, cmp = lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        
        dp = []
        for i in range(len(nums)):
            l, r = 0, len(dp) - 1
            while l <= r:
                mid = (l + r) / 2
                # 注意这边是< 而不是<=因为等于的话，大的数还在他之前
                if dp[mid][1] < nums[i][1]:
                    l = mid + 1
                else:
                    r = mid - 1
            if l < len(dp):
                dp[l] = nums[i]
            else:
                dp.append(nums[i])
        return len(dp)