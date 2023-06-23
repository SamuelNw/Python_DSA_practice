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

import numpy as np
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


def all_construct_tab(target: str, wordBank: List[list]) -> List[list]:
    table = [[]] * (len(target) + 1)
    table[0] = [[]]

    for i in range(len(table)):
        for word in wordBank:
            if target[i: i + len(word)] == word:
                combinations = list(
                    map(lambda lst: lst + [word], table[i]))
                for value in combinations:
                    table[i+len(word)].append(value)

    return set(table[-1])


print(all_construct("purple", ["purp", "le", "p", "purpl", "ur"]))
print(all_construct_tab("purple", ["purp", "le", "p", "purpl", "ur"]))
# print(all_construct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaazz",
#       ["aaa", "a", "aa", "aaaaaaa", "aaaaa"]))
