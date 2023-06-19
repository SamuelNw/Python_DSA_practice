"""
Given an array of integers, and an integer target, return an array of all numbers
in the array that can sum up to target, or None if no such numbers. Any number can
be used as many times as possible.
"""


def how_sum(numbers: list, target: int, memo={}) -> list:
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        rem = target - num
        res = how_sum(numbers, rem, memo)
        if res != None:
            memo[target] = res + [num]
            return memo[target]

    memo[target] = None
    return None


print(how_sum([7, 14], 300))
