"""
Given an array of integers, and an integer target, return the shortest array of all numbers
in the array that can sum up to target, or None if no such numbers. Any number can
be used as many times as possible.
"""


def best_sum(numbers: list, target: int, memo={}) -> bool:
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest = None

    for num in numbers:
        rem = target - num
        res = best_sum(numbers, rem, memo)

        if res != None:
            comb = res + [num]
            if shortest == None or len(comb) < len(shortest):
                shortest = comb
                memo[target] = shortest

    memo[target] = shortest
    return shortest


def best_sum_tab(numbers: list, target: int) -> list:
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target):
        if table[i] != None:
            for num in numbers:
                comb = table[i] + [num]
                if (i + num <= target) and (not (table[i+num]) or len(comb) < len(table[i + num])):
                    table[i+num] = comb

    return table[target]


"""
Complexity analysis (Both methods):
TC -> O(m * m * n)
SC -> O(m * m)

where:
m = target
n = length of numbers array.
"""

print(best_sum([2, 3, 5], 8))   # -> [5, 3]
print(best_sum_tab([2, 3, 5], 8))   # -> [5, 3]
