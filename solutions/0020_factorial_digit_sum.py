"""
title : 0020_factorial_digit_sum.py
create : @tarickali 23/06/13
update : @tarickali 23/06/13

Problem Description:
--------------------
n! means n x (n - 1) x ... x 3 x 2 x 1.

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum
of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!.
"""


def factorial(n: int) -> int:
    f = 1
    for i in range(n):
        f *= i + 1
    return f


def solution(n: int) -> int:
    f = str(factorial(n))
    return sum(int(d) for d in f)


if __name__ == "__main__":
    sol = solution(100)
    print(sol)
