# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys
# in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
# and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has
# the prefix prefix, and false otherwise.

# Runtime: 282 ms, faster than 35.42% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 31.7 MB, less than 38.07% of Python3 online submissions for Implement Trie (Prefix Tree).


class Trie_Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = Trie_Node("")

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Trie_Node(char)
                node.children[char] = new_node
                node = new_node
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if node.end_of_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # // return True
    print(trie.search("app"))  # // return False
    print(trie.startsWith("app"))  # // return True
    trie.insert("app")
    print(trie.search("app")) # // return True
