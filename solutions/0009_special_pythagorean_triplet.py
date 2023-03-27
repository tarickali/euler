"""
title : 0009_special_pythagorean_triplet.py
create : @tarickali 23/03/27
update : @tarickali 23/03/27

Problem Description:
--------------------
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def solution() -> int:
    N = 1000
    for c in range(N - 1, 0, -1):
        b = c - 1
        a = N - c - b
        while 1 < a < b < c:
            if a**2 + b**2 == c**2:
                return a * b * c
            b -= 1
            a += 1


if __name__ == "__main__":
    sol = solution()
    print(sol)
