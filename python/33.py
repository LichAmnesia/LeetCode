# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-30 02:03:26
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-30 02:03:28


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 1:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            # handle left part
            if nums[mid] >= nums[left]:
                if target < nums[mid] and target >= nums[left]:  # target in left part
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:  # target in right part
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
