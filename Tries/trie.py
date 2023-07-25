"""
Implementation of a Trie.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        """Adds a word to the word dictionary."""
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = char
            current = current.children[char]

        current.end_of_word = True

    def starts_with(self, prefix: str) -> bool:
        """Checks if the input word is a prefix of any word in the dictionary."""
        current = self.root

        for p in prefix:
            if p not in current.children:
                return False
            current = current.children[p]

        return True

    def search(self, target: str) -> bool:
        """Returns True if target is found else false."""
        current = self.root

        for char in target:
            if char not in current.children:
                return False
            current = current.children[char]

        return current.end_of_word

    def search_alpha(self, target: str) -> bool:
        """
        Returns true if there is any string in the data structure that matches
        word or false otherwise. word may contain dots '.' where dots can
        be matched with any letter.
        """
        def dfs(j: int, root: TrieNode) -> bool:
            current = root

            for i in range(j, len(target)):
                c = target[i]

                if c == ".":
                    for child in current.children.values():
                        if (dfs(i + 1, child)):
                            return True
                    return False
                else:
                    if c not in current.children:
                        return False
                    current = current.children[c]

            return current.end_of_word

        return dfs(0, self.root)
