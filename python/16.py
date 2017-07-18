# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-02 17:32:20
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-02 17:42:46


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

        self.ans = sys.maxint
        nums = sorted(nums)
        
        def search(l, r, val, target):
            while l < r:
                sum_ = nums[l] + nums[r] + val
                if abs(sum_ - target) < abs(self.ans - target):
                    self.ans = sum_
                # Why should delete?
                # while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                #     l += 1
                # while r > 0 and nums[r] == nums[r - 1]:
                #     r -= 1
                if sum_ < target:
                    l += 1
                else:
                    r -= 1

        i = 0
        while i < len(nums) - 2:
            search(i + 1, len(nums) - 1, nums[i], target)
            while i < len(nums) - 2 and nums[i + 1] == nums[i]:
                i += 1
            i += 1


        

        return self.ans
