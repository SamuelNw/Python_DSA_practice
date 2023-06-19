"""
Given an array of integers, and an integer target, return True
if any of the numbers in the array can sum up to target. Any number can
be used as many times as possible.
"""


def can_sum(numbers, target, memo={}):
    if target in memo:
        return memo[target]
    if (target == 0):
        return True
    if target < 0:
        return False

    for num in numbers:
        rem = target - num
        if (can_sum(numbers, rem, memo)) == True:
            memo[rem] = True
            return True

    memo[target] = False
    return False


print(can_sum([14, 7], 28))
