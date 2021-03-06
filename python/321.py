# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Date:   2017-01-02 13:57:50
# @Last Modified by:   Lich_Amnesia
# @Last Modified time: 2017-01-02 13:57:57
# @Email: shen.huang@colorado.edu
# http://bookshadow.com/weblog/2015/12/24/leetcode-create-maximum-number/

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMax(nums, t):
            ans = []
            size = len(nums)
            for i in range(size):
                while ans and len(ans) + size - i > t and ans[-1] < nums[i]:
                    ans.pop()
                if len(ans) < t:
                    ans += nums[i],
                    
            return ans
            
        def merge(nums1, nums2):
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans += nums1[0],
                    nums1 = nums1[1:]
                else:
                    ans += nums2[0],
                    nums2 = nums2[1:]
            return ans
            
        len1, len2 = len(nums1), len(nums2)
        res = []
        for x in range(max(0, k - len2), min(k, len1) + 1):
            tmp = merge(getMax(nums1, x), getMax(nums2, k - x))
            res = max(tmp, res)
        return res