# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-06 00:04:41
# @Last Modified time: 2016-10-06 00:38:54
# @FileName: 81.py


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) < 1:
            return False
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                if nums[l] <= target and nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[r] > nums[mid]:
                if nums[mid] < target and nums[r] > target:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[l] == nums[mid]:
                l += 1
            elif nums[r] == nums[mid]:
                r -= 1
            else:
                print "ss"
        return False