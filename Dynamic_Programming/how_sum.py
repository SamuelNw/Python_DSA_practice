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


def how_sum_tab(numbers: list, target: int) -> list:
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target):
        if table[i] != None:
            for num in numbers:
                if i + num <= target:
                    table[i+num] = table[i] + [num]

    return table[target]


"""
Complexity analysis (Both methods):
TC -> O(m * m * n)
SC -> O(m * m)

where:
m = target
n = length of numbers array.
"""


print(how_sum([7, 14], 300))
print(how_sum_tab([5, 4, 3], 7))    # [4, 3]
