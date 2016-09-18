# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-17 09:19:22
# @Last Modified time: 2016-09-17 10:13:29
# @FileName: 349.py


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = set()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i, j = i + 1, j + 1
            while i < len(nums1) and j < len(nums2) and nums1[i] < nums2[j]:
                i += 1
            while i < len(nums1) and j < len(nums2) and nums1[i] > nums2[j]:
                j += 1
        return list(res)
            