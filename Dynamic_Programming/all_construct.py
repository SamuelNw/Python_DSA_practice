"""
A function that takes in a string (target), and an array of strings (wordBank). It returns a 2D array of
all the possible ways that the target can be constructed by concatenating elements of the wordbank array.
Each element of the 2D array should represent one combination that constructs the target.

Elements of wordBank may be reused as many times as you need.

If no available combinations, return an empty array. If target is an empty string, return an array with
an empty array inside it (an empty 2D array).

Example:

Input:
target, wordBank = "purple", ["purp", "le", "p", "purpl", "ur"]

Output:
[
    ["purp", "le"],
    ["p", "ur", "p", "le"]
]
"""

from typing import List


def all_construct(target: str, wordBank: List[list], memo={}) -> List[list]:
    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    res = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixWays = all_construct(suffix, wordBank, memo)
            targetWays = [[word] + s for s in suffixWays]
            for value in targetWays:
                res.append(value)

    memo[target] = res

    return memo[target]


print(all_construct("purple", ["purp", "le", "p", "purpl", "ur"]))
print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      ["aaa", "a", "aa", "aaaaaaa", "aaaaa"]))
