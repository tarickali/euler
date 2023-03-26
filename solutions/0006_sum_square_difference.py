"""
title : 0006_sum_square_difference.py
create : @tarickali 23/03/26
update : @tarickali 23/03/26

Problem Description:
--------------------
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def solution() -> int:
    N = 100
    sum_of_squares = 0
    square_of_sums = 0

    for i in range(1, N + 1):
        sum_of_squares += i**2
        square_of_sums += i
    square_of_sums **= 2

    return square_of_sums - sum_of_squares


if __name__ == "__main__":
    sol = solution()
    print(sol)
