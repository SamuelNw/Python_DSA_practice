"""
Given an array of distinct integers candidates and a target integer target, return a list of
all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers
is different.

The test cases are generated such that the number of unique combinations that sum
up to target is less than 150 combinations for the given input.

"""

from typing import List


def combinationSum(nums: list, target: int) -> List[List[int]]:
    table = [[] for _ in range(target + 1)]
    table[0] = [[]]

    for num in nums:
        for i in range(1, len(table)):
            if (i - num) >= 0:
                for combination in table[i - num]:
                    table[i].append(combination + [num])

    return table[target]


"""
Complexity Analysis:
TC -> O(len(nums) * target)
SC -> O(target)
"""


# Returns -> [[2, 2, 3], [3, 4], [7]]
print(combinationSum([2, 3, 4, 7], 7))
