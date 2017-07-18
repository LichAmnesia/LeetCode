# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-20 15:19:50
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-20 15:19:52



import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n, m = len(nums1), len(nums2)
        if n is 0 or m is 0:
            return []
        heap, k_small = [(nums1[0] + nums2[i], 0, i) for i in range(m)], []
        heapq.heapify(heap)
        while len(k_small) < k and len(heap) > 0:
            sum_, i, j = heapq.heappop(heap)
            k_small.append([nums1[i], nums2[j]])
            if i + 1 < n:
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
        return k_small