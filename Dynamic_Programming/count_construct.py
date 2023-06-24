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


def count_construct_tab(wordBank: list, target: str) -> int:
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(table)):
        if table[i] != 0:
            for word in wordBank:
                if target[i:i+len(word)] == word:
                    table[i + len(word)] += table[i]

    return table[-1]


"""
Complexity analysis (Both methods):
TC -> O(m * m * n)
SC -> O(m)

where:
m = target
n = length of wordBank array.
"""


print(count_construct(["ab", "abc", "cd", "def", "abcd"], "abcdef"))    # -> 1
print(count_construct(["e", "eee", "eeeeee", "eeeeeeeee",
      "eeeeeeeeeeeeeeeeee"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"))  # -> 0

print(count_construct_tab(
    ["ab", "abc", "cd", "def", "abcd"], "abcdef"))     # -> 1
print(count_construct_tab(["e", "eee", "eeeeee", "eeeeeeeee",
      "eeeeeeeeeeeeeeeeee"], "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef"))   # -> 0
