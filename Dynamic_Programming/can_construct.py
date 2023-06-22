"""
write a function that takes in a string and an array of strings and returns True if
the string can be built from concatenating any number of words from the array, or False
otherwise.
"""


def can_construct(string: str, wordBank: list, memo={}) -> bool:
    if string in memo:
        return memo[string]
    if string == "":
        return True

    for word in wordBank:
        if string.startswith(word):
            suffix = string[len(word):]
            if (can_construct(suffix, wordBank, memo)) == True:
                memo[string] = True
                return True

    memo[string] = False
    return False


def can_construct_tab(string: str, wordBank: list) -> bool:
    table = [False] * (len(string) + 1)
    table[0] = True

    for i in range(len(table)):
        if table[i] == True:
            for word in wordBank:
                if string[i: i + len(word)] == word:
                    if i + len(word) <= len(table):
                        table[i+len(word)] = True

    return table[-1]


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(can_construct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
