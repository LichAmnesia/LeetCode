# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-28 16:06:47
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-28 16:06:50


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hash:
            return False
        self.hash[val] = len(self.nums)
        self.nums.append(val)
        # print self.hash, self.nums
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.hash:
            return False
        # print self.hash[val], val, len(self.nums), len(self.hash)
        self.nums[self.hash[val]] = self.nums[-1]
        self.hash[self.nums[-1]] = self.hash[val]
        self.nums.pop()
        del self.hash[val]
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
