# -*- coding: utf-8 -*-
# @Author: Lich_Amnesia
# @Email: alwaysxiaop@gmail.com
# @Date:   2016-10-21 22:52:26
# @Last Modified time: 2016-10-21 22:52:40
# @FileName: 211.py

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
        
        def dfs(root, word):
            # print word
            
            if len(word) < 1:
                return root.isWord
            if len(root.child) < 1:
                return False
            letter = word[0]
            
            if letter == '.':
                return any([dfs(root.child[node], word[1:]) for node in root.child])
            else:
                node = root.child.get(letter, None)
                if node is None:
                    return False
                else:
                    return dfs(node, word[1:])
        # return node.isWord
        return dfs(node, word)

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

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = Trie()
        # trie.insert("somestring")
        # trie.search("key")

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")