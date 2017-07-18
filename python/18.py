# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-07 00:13:33
# @Last Modified time: 2016-10-07 00:25:10
# @FileName: 18.py


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        ans = []
        nums = sorted(nums)
        
        def search(l, r, target1, target2):
            while l < r:
                sum_ = nums[l] + nums[r] + target1 + target2
                if sum_ == target:
                    ans.append([target1, target2, nums[l], nums[r]])
                    while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif sum_ < target:
                    l += 1
                else:
                    r -= 1

        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                search(j + 1, len(nums) - 1, nums[i], nums[j])
                while j < len(nums) - 2 and nums[j + 1] == nums[j]:
                    j += 1
                j += 1
            while i < len(nums) - 3 and nums[i + 1] == nums[i]:
                i += 1
            i += 1


        

        return ans
