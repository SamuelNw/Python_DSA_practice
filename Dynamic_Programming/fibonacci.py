"""
Memoization.
- Function returns the nth number in the fib series.

Time Complexity --> O(n)
"""


def fib(n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# tabulation solution:
def fib_tab(n: int) -> int:
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(n):
        if i+1 <= n:
            table[i+1] += table[i]
        if i+2 <= n:
            table[i+2] += table[i]

    return table[n]


"""
Complexity analysis (Both methods):
TC -> O(n)
SC -> O(n)
"""


# Computes and returns asap.
print(fib(999))
print(fib_tab(999))
