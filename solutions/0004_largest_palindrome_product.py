"""
title : 0004_largest_palindrome_product.py
create : @tarickali 23/03/25
update : @tarickali 23/03/25

Problem Description:
--------------------
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


def solution() -> int:
    best = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            k = i * j
            if is_palindrome(k) and k > best:
                best = k
    return best


if __name__ == "__main__":
    sol = solution()
    print(sol)
