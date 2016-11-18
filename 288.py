# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-11-17 16:26:09
# @Last Modified time: 2016-11-17 16:34:13
# @FileName: 288.py


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = collections.defaultdict(list)
        for word in dictionary:
            if len(word) < 1:
                self.dic[""].append(word)
            else:
                self.dic[word[0] + str(len(word) - 2) + word[-1]].append(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) < 1: 
            return True
        key = word[0] + str(len(word) - 2) + word[-1]
        print self.dic.get(key,0)
        if key not in self.dic:
            return True
        else:
            return all(word == w for w in self.dic[key])
