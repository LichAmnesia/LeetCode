# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 16:38:52
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-02 17:32:15


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

        ans = []
        nums = sorted(nums)
        
        def search(l, r, target):
            while l < r:
                sum_ = nums[l] + nums[r] + target
                if sum_ == 0:
                    ans.append([target, nums[l], nums[r]])
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif sum_ < 0:
                    l += 1
                else:
                    r -= 1

        i = 0
        while i < len(nums) - 2:
            search(i + 1, len(nums) - 1, nums[i])
            while i < len(nums) - 2 and nums[i + 1] == nums[i]:
                i += 1
            i += 1


        

        return ans
