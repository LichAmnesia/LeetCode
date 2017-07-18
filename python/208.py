# -*- coding: utf-8 -*-
# @Author: Lich Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-11 20:47:08
# @Last Modified by:   Lich Amnesia
# @Last Modified time: 2016-10-11 21:00:22


class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = dict()
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            chi = node.child.get(letter, None)
            if chi is None:
                chi = TrieNode()
                node.child[letter] = chi
            node = chi
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            node = node.child.get(letter, None)
            if node is None:
                return False
        return node.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            node = node.child.get(letter, None)
            if node is None:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")