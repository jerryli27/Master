# This trie class comes from leetcode forum.

import collections

# 
class TrieNode(object):
    def __init__(self):
        self.is_phrase = False
        self.children = collections.defaultdict(TrieNode)
    # Returns None if the node does not have such a child with name = word. Return that child if it has it.
    def has_child(self, word):
        if word not in self.children:
            return None
        else:
            return self.children[word]
class Trie(object):
    def __init__(self, init_list = None):
        self.root = TrieNode()
        for item in init_list:
            self.insert(item)

    def insert(self, phrase):
        node = self.root
        for word in phrase.split(' '):
            node = node.children[word]
        node.is_phrase = True

    def search(self, phrase, is_phrase=True):
        node = self.root
        for word in phrase.split(' '):
            if word not in node.children:
                return False
            node = node.children[word]
        return (node.is_phrase if is_phrase else True, node)

    def starts_with(self, prefix):
        return self.search(prefix, False)
