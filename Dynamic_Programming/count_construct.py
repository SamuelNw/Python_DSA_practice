"""
write a function that takes in a string and an array of strings and returns the
number of ways that the words in the array can be concatenated to create the
given string, words can be reused as many times as possible.
"""


def count_construct(wordBank: list, target: str, memo={}) -> int:
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    res = 0

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            ways = count_construct(wordBank, suffix, memo)
            res += ways

    memo[target] = res
    return res


print(count_construct(["ab", "abc", "cd", "def", "abcd"], "abcdef"))
print(count_construct(["e", "eee", "eeeeee", "eeeeeeeee",
      "eeeeeeeeeeeeeeeeee"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"))
