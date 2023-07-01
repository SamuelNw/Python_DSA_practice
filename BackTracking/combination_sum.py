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
    res = []

    def dfs(arr: list, cur_index: int, cur_sum: int, cur_combination: List[int], target: int) -> None:
        if cur_sum == target:
            res.append(cur_combination)
            return

        if cur_sum > target:
            return

        for i in range(cur_index, len(arr)):
            dfs(arr, i, cur_sum + arr[i], cur_combination + [arr[i]], target)

    dfs(nums, 0, 0, [], target)

    return res


"""
Complexity Analysis:
TC -> O(2 ^ n) where n is len(nums)
SC -> O(2 ^ n)
"""


# Returns -> [[2, 2, 3], [3, 4], [7]]
print(combinationSum([2, 3, 4, 7], 7))
