# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-09-23 20:21:55
# @Last Modified time: 2016-09-23 20:31:55
# @FileName: 167.py


class Solution(object):

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        head = 0
        tail = len(numbers) - 1
        while head < tail and numbers[head] + numbers[tail] != target:
            if numbers[head] + numbers[tail] > target:
                tail -= 1
            else:
                head += 1
        return [head + 1, tail + 1]
