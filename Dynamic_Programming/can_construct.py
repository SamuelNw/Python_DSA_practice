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


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
