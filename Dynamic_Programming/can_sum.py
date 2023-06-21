"""
Given an array of integers, and an integer target, return True
if any of the numbers in the array can sum up to target. Any number can
be used as many times as possible.
"""


def can_sum(numbers: list, target: int, memo={}) -> bool:
    if target in memo:
        return memo[target]
    if (target == 0):
        return True
    if target < 0:
        return False

    for num in numbers:
        rem = target - num
        if (can_sum(numbers, rem, memo)) == True:
            memo[target] = True
            return True

    memo[target] = False
    return False


# Can_sum tabulation method:
def can_sum_tab(numbers: list, target: int) -> bool:
    table = [False] * (target + 1)
    table[0] = True

    for i in range(target):
        if table[i] == True:
            for num in numbers:
                if (i + num) <= target:
                    table[i+num] = True

    return table[target]


print(can_sum([14, 7], 300))
print(can_sum_tab([14, 7], 300))
