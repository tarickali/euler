"""
title : 0001_multiples_of_3_or_5.py
create : @tarickali 23/03/24
update : @tarickali 23/03/24

Problem Description:
--------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def solution() -> int:
    N = 1000
    total = 0
    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


if __name__ == "__main__":
    sol = solution()
    print(sol)
