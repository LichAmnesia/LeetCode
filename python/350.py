# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-15 23:56:48
# @Last Modified time: 2016-09-16 00:02:39
# @FileName: 350.py


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            while i < len(nums1) and nums1[i] < nums2[j]:
                i += 1
            while i < len(nums1) and j < len(nums2) and nums1[i] > nums2[j]:
                j += 1
            if i < len(nums1) and j < len(nums2) and nums1[i] == nums2[j]:
                res.append(nums1[i])
                i, j = i + 1, j + 1
        return res