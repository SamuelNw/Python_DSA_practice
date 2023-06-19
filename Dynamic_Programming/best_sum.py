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
        res = best_sum(numbers, rem)

        if res != None:
            comb = res + [num]
            if shortest == None or len(comb) < len(shortest):
                shortest = comb
                memo[target] = shortest

    memo[target] = shortest
    return shortest


print(best_sum([7, 14], 150))
