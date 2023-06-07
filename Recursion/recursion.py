"""
    - Recursion practice with different functions
"""


# Reversing a string.
def reverse_string(value):
    if value == "":
        return ""

    return reverse_string(value[1:]) + value[0]


# Check if a string is a palindrome.
def is_palindrome(value):
    if len(value) == 0 or len(value) == 1:
        return True

    if value[0] == value[-1]:
        return is_palindrome(value[1:-1])
    else:
        return False

# Conversion of decimals to binary.


def decimal_to_binary(decimal, result=""):
    if decimal < 1:
        return result
    result = str(decimal % 2) + result
    return decimal_to_binary(decimal//2, result)

# Summation of Natural numbers


def number_summation(num):
    if num <= 1:
        return num
    return num + number_summation(num - 1)

# Unoptimized fib series


def fib_num(num):
    if num == 1 or num == 0:
        return num
    return fib_num(num - 1) + fib_num(num - 2)


# print(decimal_to_binary(233, ""))           #should return "1001011"
# print(number_summation(10))                 #should return 55
print(fib_num(9))
